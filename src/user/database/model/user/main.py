from sqlalchemy.orm import Mapped, mapped_column

from src.base.database.model.base import Base


class User(Base):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(
        "name", nullable=False, unique=True
    )

    def __repr__(self) -> str:
        return f"User()"
