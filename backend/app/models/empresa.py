from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Empresa(Base):
    __tablename__ = "empresa"

    id: Mapped[int]
    nombre: Mapped[str]