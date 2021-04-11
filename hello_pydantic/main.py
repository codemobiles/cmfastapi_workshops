from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic import ValidationError
from pydantic import validator


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    @validator('id')
    def checkId(cls, v):
        if v < 0:
            raise ValueError('must more than or equal zero')
        return v

external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))


try:
    u = User(id=1, signup_ts='2019-06-01 12:22', friends=[1, 2, 3])
    print(u)
    u2 = User(id=0, signup_ts='2019-06-01 12:22', friends=[1, 2, 3])
except ValidationError as e:
    print(e.json())


print(user.schema_json(indent=2))