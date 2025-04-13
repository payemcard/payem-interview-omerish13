from pydantic import BaseModel
from enum import Enum
import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseModel):
            return obj.dict()
        if isinstance(obj, Enum):
            return obj.value
        return super().default(obj)


def object_hook(obj):
    if 'request_type' in obj:
        obj['request_type'] = RequestType(obj['request_type'])
    return obj


class CustomJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=object_hook, *args, **kwargs)


class RequestType(str, Enum):
    PURCHASE = "Purchase"
    REIMBURSEMENT = "Reimbursement"

class Request(BaseModel):
    id: int
    name: str
    description: str
    amount: float
    currency: str
    employee_name: str
    status: str
    created_at: str
    updated_at: str = ""
    approved_amount: float = 0.0
    request_type: RequestType = None