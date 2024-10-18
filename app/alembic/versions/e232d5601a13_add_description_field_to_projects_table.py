"""Add description field to projects table

Revision ID: e232d5601a13
Revises: b71f48b119c0
Create Date: 2024-10-17 01:46:28.739508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e232d5601a13'
down_revision: Union[str, None] = 'b71f48b119c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Añadir columna `description` a la tabla `projects`
    op.add_column('projects', sa.Column(
        'description', sa.String(), nullable=True))


def downgrade() -> None:
    # Eliminar columna `description` de la tabla `projects` si es necesario revertir
    op.drop_column('projects', 'description')
