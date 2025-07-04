"""add browser_session_id to tasks, workflow_runs and task v2 tables

Revision ID: f63892bfc429
Revises: 6cf2c1e15039
Create Date: 2025-07-03 18:37:32.199437+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f63892bfc429"
down_revision: Union[str, None] = "6cf2c1e15039"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("observer_cruises", sa.Column("browser_session_id", sa.String(), nullable=True))
    op.create_index(
        op.f("ix_observer_cruises_browser_session_id"), "observer_cruises", ["browser_session_id"], unique=False
    )
    op.add_column("tasks", sa.Column("browser_session_id", sa.String(), nullable=True))
    op.create_index(op.f("ix_tasks_browser_session_id"), "tasks", ["browser_session_id"], unique=False)
    op.add_column("workflow_runs", sa.Column("browser_session_id", sa.String(), nullable=True))
    op.create_index(op.f("ix_workflow_runs_browser_session_id"), "workflow_runs", ["browser_session_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_workflow_runs_browser_session_id"), table_name="workflow_runs")
    op.drop_column("workflow_runs", "browser_session_id")
    op.drop_index(op.f("ix_tasks_browser_session_id"), table_name="tasks")
    op.drop_column("tasks", "browser_session_id")
    op.drop_index(op.f("ix_observer_cruises_browser_session_id"), table_name="observer_cruises")
    op.drop_column("observer_cruises", "browser_session_id")
    # ### end Alembic commands ###
