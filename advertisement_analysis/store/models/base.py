from sqlalchemy import func

from advertisement_analysis.store import db


class _EntityBase(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
