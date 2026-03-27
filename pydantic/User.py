from datetime import datetime
from pydantic import BaseModel, PositiveInt, EmailStr
from typing import Optional


class User(BaseModel):
    id: PositiveInt
    name: str = 'John Doe'
    age: PositiveInt
    email: EmailStr
    signup_ts : datetime | None
    is_active: bool = True
    nickname: Optional[str] = None
    tastes: dict[str, PositiveInt]


# Pydantic automatically validates and converts data
external_data = {
    'id': '1',
    'age': '38',
    'email': 'edgaromarsfgmail.com',
    'signup_ts': '2019-06-01 12:22',
    'tastes': {
        'wine': 9,
        b'cheese': 7,
        'cabbagge': '1',
    },
}

user = User(**external_data)

print(user.id)
print(user.model_dump())
print(user.model_dump_json())