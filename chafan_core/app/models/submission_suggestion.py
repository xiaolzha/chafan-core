from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import CHAR, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import JSON

from chafan_core.db.base_class import Base
from chafan_core.utils.base import UUID_LENGTH
from chafan_core.utils.constants import editor_T
from chafan_core.utils.validators import StrippedNonEmptyStr

if TYPE_CHECKING:
    from . import *  # noqa: F401, F403


class SubmissionSuggestion(Base):
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(CHAR(length=UUID_LENGTH), index=True, unique=True, nullable=False)

    author_id = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    author: "User" = relationship(
        "User", back_populates="submission_suggestions", foreign_keys=[author_id]
    )  # type: ignore

    title: StrippedNonEmptyStr = Column(String, nullable=False)
    description = Column(String)
    description_text = Column(String)
    description_editor: editor_T = Column(String)
    topic_uuids: Optional[List[str]] = Column(JSON)  # type: ignore
    created_at = Column(DateTime(timezone=True), nullable=False)

    comment = Column(String)

    status = Column(String, nullable=False, default="pending")
    accepted_at = Column(DateTime(timezone=True))
    rejected_at = Column(DateTime(timezone=True))
    retracted_at = Column(DateTime(timezone=True))
    accepted_diff_base = Column(JSON)  # None when not accepted yet

    submission_id = Column(
        Integer, ForeignKey("submission.id"), nullable=False, index=True
    )
    submission: "Submission" = relationship("Submission", back_populates="submission_suggestions", foreign_keys=[submission_id])  # type: ignore
