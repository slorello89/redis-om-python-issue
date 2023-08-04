import datetime
from typing import Optional
from pydantic import EmailStr
from redis_om import HashModel

class Customer(HashModel):
    first_name: str
    last_name: str
    email: EmailStr
    join_date: datetime.date
    age: int
    bio: Optional[str]