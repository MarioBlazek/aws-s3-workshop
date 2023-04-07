from pydantic import BaseModel
from datetime import datetime


class AwsS3Bucket(BaseModel):
    name: str
    created: datetime


class AwsAccount(BaseModel):
    id: str
    arn: str
    user_id: str


class AwsS3Object(BaseModel):
    name: str
    size: int
