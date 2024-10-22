from pydantic import BaseModel


class Case(BaseModel):
    id: int
    name: str
    description: str
    steps: list[str]
    expected_result: str
    priority: str