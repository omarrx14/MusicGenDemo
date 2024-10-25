from alembic.config import Config
from alembic import command

# Configurar la ruta al archivo alembic.ini
alembic_cfg = Config("alembic.ini")
# Aplica todas las migraciones hasta el último commit
command.upgrade(alembic_cfg, "head")
