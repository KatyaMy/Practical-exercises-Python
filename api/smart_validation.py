from pydantic import BaseModel
from faker import Faker

faker = Faker()


def generate_name():
    faker.name()


user_dict = {"name": faker.name(), "age": 30}


class User(BaseModel):
    name: str
    age: int


print(User(**user_dict).model_dump())
