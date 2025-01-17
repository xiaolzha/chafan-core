import datetime
from typing import Any, List

from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

from chafan_core.app import crud, schemas
from chafan_core.app.api import deps
from chafan_core.app.cache_controllers.site_profiles import CachedSiteProfiles
from chafan_core.app.cached_layer import CachedLayer
from chafan_core.app.common import OperationType, is_dev
from chafan_core.app.endpoint_utils import get_site
from chafan_core.app.limiter import limiter
from chafan_core.app.materialize import check_user_in_site, user_schema_from_orm
from chafan_core.app.schemas.event import EventInternal, InviteJoinSiteInternal
from chafan_core.utils.base import HTTPException_, unwrap

router = APIRouter()


if is_dev():

    @router.get("/", response_model=List[schemas.User], include_in_schema=False)
    def read_users(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
    ) -> Any:
        """
        Retrieve users as super user.
        """
        users = crud.user.get_multi(db, skip=skip, limit=limit)
        return [user_schema_from_orm(u) for u in users]

    @router.post("/", response_model=schemas.User, include_in_schema=False)
    def create_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.UserCreate,
    ) -> Any:
        """
        Create new user as super user.
        """
        user = crud.user.get_by_email(db, email=user_in.email)
        if user:
            raise HTTPException_(
                status_code=400,
                detail="The user with this email already exists in the system.",
            )
        return user_schema_from_orm(crud.user.create(db, obj_in=user_in))


@router.post("/invite", response_model=schemas.GenericResponse)
@limiter.limit("60/minute")
def invite_new_user(
    response: Response,
    request: Request,
    *,
    cached_layer: CachedLayer = Depends(deps.get_cached_layer_logged_in),
    db: Session = Depends(deps.get_db),
    user_invite_in: schemas.UserInvite,
) -> Any:
    """
    Invite internal user by id to a site.
    """
    site = None
    # if the site is specified, first check whether the current user is allowed to add new member to site
    site = get_site(db, user_invite_in.site_uuid)
    check_user_in_site(
        db,
        site=site,
        user_id=cached_layer.unwrapped_principal_id(),
        op_type=OperationType.AddSiteMember,
    )
    utc_now = datetime.datetime.now(tz=datetime.timezone.utc)
    # Whether the user is a new external user (invited by email)

    assert user_invite_in.user_uuid is not None and site is not None
    invited_user = crud.user.get_by_uuid(db, uuid=user_invite_in.user_uuid)
    if not invited_user:
        raise HTTPException_(
            status_code=400,
            detail="The user doesn't exist.",
        )

    existing_profile = crud.profile.get_by_user_and_site(
        db, owner_id=invited_user.id, site_id=site.id
    )
    if not existing_profile:
        CachedSiteProfiles.create_site_profile(
            cached_layer, owner=invited_user, site_uuid=site.uuid
        )
        application = crud.application.get_by_applicant_and_site(
            db, applicant=invited_user, site=site
        )
        if application is not None:
            crud.application.update(
                db,
                db_obj=application,
                obj_in=schemas.ApplicationUpdate(pending=False),
            )
        crud.notification.create_with_content(
            cached_layer.broker,
            receiver_id=invited_user.id,
            event=EventInternal(
                created_at=utc_now,
                content=InviteJoinSiteInternal(
                    subject_id=cached_layer.unwrapped_principal_id(),
                    site_id=site.id,
                    user_id=invited_user.id,
                ),
            ),
        )
    return schemas.GenericResponse()


if is_dev():

    @router.get("/{user_id}", response_model=schemas.User, include_in_schema=False)
    def read_user_by_id(
        user_id: int,
        db: Session = Depends(deps.get_db),
    ) -> Any:
        """
        Get a specific user by id as super user.
        """
        return user_schema_from_orm(unwrap(crud.user.get(db, id=user_id)))

    @router.put("/{user_id}", response_model=schemas.User, include_in_schema=False)
    def update_user(
        *,
        db: Session = Depends(deps.get_db),
        user_id: int,
        user_in: schemas.UserUpdate,
    ) -> Any:
        """
        Update a user as super user.
        """
        user = crud.user.get(db, id=user_id)
        if not user:
            raise HTTPException_(
                status_code=404,
                detail="The user with this username does not exist in the system",
            )
        user = crud.user.update(db, db_obj=user, obj_in=user_in)
        return user_schema_from_orm(user)
