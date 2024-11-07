from typing import Dict

from fastapi import APIRouter

from project.infrastructure.postgres.database import PostgresDatabase

from project.infrastructure.postgres.repository.disease_repo import DiseaseRepository
from project.schemas.disease import DiseaseSchema

router = APIRouter()

@router.get("/all_diseases", response_model=list[DiseaseSchema])
async def get_all_users() -> list[DiseaseSchema]:
    disease_repo = DiseaseRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await disease_repo.check_connection(session=session)
        all_diseases = await disease_repo.get_all_deseases(session=session)

    return all_diseases


@router.post("/disease", response_model=DiseaseSchema)
async def save_disease(disease: DiseaseSchema) -> DiseaseSchema:
    disease_repo = DiseaseRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await disease_repo.check_connection(session=session)
        result = await disease_repo.save_disease(disease=disease, session=session)

    return result

@router.put("/disease", response_model=DiseaseSchema)
async def update_disease(disease: DiseaseSchema) -> DiseaseSchema:
    disease_repo = DiseaseRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await disease_repo.check_connection(session=session)
        result = await disease_repo.update_disease(disease=disease, session=session)

    return result


@router.delete("/disease")
async def update_disease(disease: DiseaseSchema) -> dict[str, bool]:
    disease_repo = DiseaseRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await disease_repo.check_connection(session=session)
        await disease_repo.delete_disease(disease=disease, session=session)

    return {"ok": True}
