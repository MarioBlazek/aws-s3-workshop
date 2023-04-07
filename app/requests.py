from pydantic import BaseModel


class AwsS3ObjectKey(BaseModel):
    key: str
