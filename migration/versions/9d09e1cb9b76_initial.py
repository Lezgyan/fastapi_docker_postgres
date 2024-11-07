from alembic import op
import sqlalchemy as sa

from project.core.config import settings


# revision identifiers, used by Alembic.
revision = '9d09e1cb9b76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('diseases',
    sa.Column('disease_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('icd_code', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('disease_id'),
    sa.UniqueConstraint('icd_code'),
    schema=settings.POSTGRES_SCHEMA
    )


def downgrade():
    op.drop_table('diseases', schema=settings.POSTGRES_SCHEMA)
