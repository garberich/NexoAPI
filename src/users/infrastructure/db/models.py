from sqlalchemy import Boolean, Column, String, Uuid

from infrastructure.db.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Uuid(as_uuid=True), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    name = Column(String(255), nullable=False)