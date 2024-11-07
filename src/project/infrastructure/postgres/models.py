from sqlalchemy.orm import Mapped, mapped_column

from project.infrastructure.postgres.database import Base


class Disease(Base):
    __tablename__ = "diseases"

    disease_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    icd_code: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
