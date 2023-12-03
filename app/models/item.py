import datetime

from sqlalchemy import (
    Column,
    String,
    DateTime,
    UUID,
    Float,
    func,
    Boolean,
    Enum,
    ForeignKey
) 

from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Item(Base):
    _tablename_ = "items"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float())

    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.now()
    )

    class Config:
        orm_mode = True