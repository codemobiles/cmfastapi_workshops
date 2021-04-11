from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic import ValidationError, validator


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    @validator('id')
    def validate_id(cls, v):
        if v < 0:
            raise ValueError('must have more than or equal zero')
        return v



external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
print(user.id)


try:
    User(id=0, signup_ts='2019-06-01 22:22', friends=[1, 2, 3])
except ValidationError as e:
    print(e.json())

print(user.schema_json(indent=2))    