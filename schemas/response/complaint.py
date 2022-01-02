from datetime import datetime

from schemas.base import BaseComplaint

from models import State


class ComplaintOut(BaseComplaint):
    id: int
    created_at: datetime
    status: State