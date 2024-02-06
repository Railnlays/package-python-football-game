from typing import TYPE_CHECKING
import uuid
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from ._team import Team


class Player(SQLModel, table=True):
    player_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        unique=True,
        index=True,
        sa_column_kwargs={"comment": "Unique identifier for the player"},
    )
    name: str
    age: int
    salary: float

    team_id: uuid.UUID | None = Field(default=None, foreign_key="team.team_id")
    team: "Team" = Relationship(back_populates="players")