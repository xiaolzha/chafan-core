import traceback
from typing import Callable, Optional, TypeVar

import sentry_sdk
from sqlalchemy.orm.session import Session

from chafan_core.app.config import settings
from chafan_core.app.data_broker import DataBroker

T = TypeVar("T")


def execute_with_db(
    db: Session, runnable: Callable[[Session], T], auto_commit: bool = True
) -> Optional[T]:
    try:
        ret = runnable(db)
        if auto_commit:
            db.commit()
        return ret
    except Exception as e:
        if settings.ENV != "dev":
            sentry_sdk.capture_exception(e)
            traceback.print_exc()
        else:
            raise e
    finally:
        db.close()
    return None


def execute_with_broker(
    runnable: Callable[[DataBroker], T],
    use_read_replica: bool = False,
    auto_commit: bool = True,
) -> Optional[T]:
    try:
        broker = DataBroker(use_read_replica=use_read_replica)
        ret = runnable(broker)
        if auto_commit and broker.db:
            broker.db.commit()
        return ret
    except Exception as e:
        if settings.ENV != "dev":
            sentry_sdk.capture_exception(e)
            traceback.print_exc()
        else:
            raise e
    finally:
        broker.close()
    return None
