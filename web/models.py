from sqlmodel import Field, SQLModel


class Coordinates(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    lat: float = Field(default=None, index=True)
    lon: float = Field(default=None, index=True)
