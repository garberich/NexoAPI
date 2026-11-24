from uuid import uuid4

from sqlalchemy import Boolean, Column, String, Uuid

from infrastructure.db.base import Base


class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)