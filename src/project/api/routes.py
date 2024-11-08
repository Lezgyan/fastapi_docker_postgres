from fastapi import APIRouter, status, HTTPException

from project.infrastructure.postgres.database import PostgresDatabase

from project.infrastructure.postgres.repository.disease_repo import DiseaseRepository
from project.schemas.disease import DiseaseSchema, DiseaseCreateUpdateSchema

from project.core.exceptions import EntityNotFound

router = APIRouter()


@router.get("/all_diseases", response_model=list[DiseaseSchema])
async def get_all_users() -> list[DiseaseSchema]:
    disease_repo = DiseaseRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        all_diseases = await disease_repo.get_all_deseases(session=session)

    return all_diseases


@router.post("/disease", response_model=DiseaseSchema)
async def save_disease(disease: DiseaseCreateUpdateSchema) -> DiseaseSchema:
    disease_repo = DiseaseRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        result = await disease_repo.save_disease(disease=disease, session=session)

    return result


@router.put("/{disease_id}", response_model=DiseaseSchema)
async def update_disease(
    disease_id: int,
    disease: DiseaseCreateUpdateSchema,
) -> DiseaseSchema:
    disease_repo = DiseaseRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        result = await disease_repo.update_disease(disease=disease, session=session)

    return result


@router.delete("/{disease_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_disease(disease_id: int) -> None:
    disease_repo = DiseaseRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            await disease_repo.delete_disease(disease_id=disease_id, session=session)
    except EntityNotFound as exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exception.message)
