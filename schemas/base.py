from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class BaseComplaint(BaseModel):
    title: str
    description: str
    amount: float