from alembic import op
import sqlalchemy as sa

from project.core.config import settings


# revision identifiers, used by Alembic.
revision = '9d09e1cb9b76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'positions',
        sa.Column('position_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'ward',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('count_bunk', sa.Integer(), nullable=False),
        sa.Column('name', sa.Text(), nullable=False),
        sa.Column('department_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['department_id'], ['departments.department_id'], ondelete='CASCADE', onupdate='CASCADE'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'operation_to_qualification_type',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('operation_type_id', sa.Integer(), nullable=False),
        sa.Column('qualification_type_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['operation_type_id'], ['operation_types.operation_type_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['qualification_type_id'], ['qualification_type.id'], ondelete='CASCADE', onupdate='CASCADE'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'course_of_treatment',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('history_id', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('receipt_date', sa.Date(), nullable=False),
        sa.Column('doctor_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['history_id'], ['medical_history.history_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['doctor_id'], ['doctors.doctor_id'], ondelete='CASCADE', onupdate='CASCADE'),
        schema=settings.POSTGRES_SCHEMA
    )


    op.create_table(
        'doctors',
        sa.Column('doctor_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('full_name', sa.String(255), nullable=False),
        sa.Column('position_id', sa.Integer(), nullable=False),
        sa.Column('department_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['position_id'], ['positions.position_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['department_id'], ['departments.department_id'], ondelete='CASCADE', onupdate='CASCADE'),
        schema=settings.POSTGRES_SCHEMA
    )


    op.create_table(
        'medicine',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'diseases',
        sa.Column('disease_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('icd_code', sa.String(50), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.UniqueConstraint('icd_code'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'medical_history',
        sa.Column('history_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('patient_id', sa.Integer(), nullable=False),
        sa.Column('disease_id', sa.Integer(), nullable=False),
        sa.Column('doctor_id', sa.Integer(), nullable=False),
        sa.Column('admission_date', sa.Date(), nullable=False),
        sa.Column('discharge_date', sa.Date(), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('ward_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['patient_id'], ['patients.patient_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['disease_id'], ['diseases.disease_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['doctor_id'], ['doctors.doctor_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['ward_id'], ['ward.id'], ondelete='CASCADE', onupdate='CASCADE'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'operation_types',
        sa.Column('operation_type_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'patient_reception',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('course_of_treatment_id', sa.Integer(), nullable=False),
        sa.Column('medication_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['course_of_treatment_id'], ['course_of_treatment.id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['medication_id'], ['medicine.id'], ondelete='CASCADE', onupdate='CASCADE'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'qualification_doctor',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('doctor_id', sa.Integer(), nullable=False),
        sa.Column('qualification_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['doctor_id'], ['doctors.doctor_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['qualification_id'], ['qualification_type.id'], ondelete='CASCADE', onupdate='CASCADE'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'departments',
        sa.Column('department_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'patients',
        sa.Column('patient_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('full_name', sa.String(255), nullable=False),
        sa.Column('date_of_birth', sa.Date(), nullable=False),
        sa.Column('snils', sa.String(20), nullable=False),
        sa.Column('medical_policy', sa.String(50), nullable=False),
        sa.UniqueConstraint('snils'),
        sa.UniqueConstraint('medical_policy'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'operations',
        sa.Column('operation_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('history_id', sa.Integer(), nullable=False),
        sa.Column('doctor_id', sa.Integer(), nullable=False),
        sa.Column('operation_type_id', sa.Integer(), nullable=False),
        sa.Column('operation_date', sa.Date(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['history_id'], ['medical_history.history_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['doctor_id'], ['doctors.doctor_id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.ForeignKeyConstraint(['operation_type_id'], ['operation_types.operation_type_id'], ondelete='CASCADE', onupdate='CASCADE'),
        schema=settings.POSTGRES_SCHEMA
    )

    op.create_table(
        'qualification_type',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.Text(), nullable=False),
        schema=settings.POSTGRES_SCHEMA
    )


def downgrade():
    op.drop_table('qualification_type', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('operations', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('patients', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('departments', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('qualification_doctor', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('patient_reception', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('operation_types', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('medical_history', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('diseases', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('medicine', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('doctors', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('course_of_treatment', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('operation_to_qualification_type', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('ward', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('positions', schema=settings.POSTGRES_SCHEMA)
