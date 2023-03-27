from typing import List
from datetime import datetime
from fastapi import FastAPI, UploadFile
from boto3 import client
from pydantic import BaseModel
import shutil
import os
from starlette.responses import FileResponse
import hashlib

app = FastAPI(title="AWS S3 Workshop API", description="Example AWS S3 endpoints to showcase what can be done.",
              version="0.0.1")
s3 = client('s3')
sts = client('sts')
bucket_name = 'marek-testing-bucket'


class AwsAccount(BaseModel):
    id: str
    arn: str
    user_id: str


class AwsS3Object(BaseModel):
    name: str
    size: int


class AwsS3ObjectKey(BaseModel):
    key: str


class AwsS3Bucket(BaseModel):
    name: str
    created: datetime


@app.get("/")
def show_welcome_message():
    """Welcome endpoint"""
    return {"Hi": "Welcome to AWS workshop #3. Today we are showcasing the S3 service. Enjoy"}


@app.get("/about/me")
def show_current_user_information() -> AwsAccount:
    """Just a simple about me route"""
    identity = sts.get_caller_identity()

    print(identity)

    return AwsAccount(id=identity['Account'], arn=identity['Arn'], user_id=identity['UserId'])


@app.get("/bucket")
def list_bucket_contents(limit: int = 10) -> List[AwsS3Object]:
    """Simple bucket listing"""
    paginator = s3.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket=bucket_name,
                                       PaginationConfig={'PageSize': limit, 'MaxItems': limit})

    objects = []

    for page in page_iterator:
        contents = page['Contents']
        for s3_obj in contents:
            objects.append(AwsS3Object(name=s3_obj['Key'], size=s3_obj['Size']))

    return objects


@app.get("/bucket/{object_id}")
def retrieve_specific_object_from_a_bucket(object_id: str) -> FileResponse:
    """Download an S3 object"""
    file_location = '/tmp/' + object_id

    s3.download_file(bucket_name, object_id, file_location)

    return FileResponse(file_location, media_type='application/octet-stream', filename=object_id)


@app.post("/bucket")
def upload_object_to_bucket(file: UploadFile):
    """Uploads a file to the S3"""

    file_name, file_extension = os.path.splitext(file.filename)
    file_name = hashlib.md5(file_name.encode()).hexdigest()

    full_file_name = file_name + file_extension
    upload_path = '/tmp/' + full_file_name

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    s3.upload_file(upload_path, bucket_name, full_file_name)
    os.remove(upload_path)

    return {"filename": full_file_name}


@app.delete("/bucket")
def delete_bucket_item(key: AwsS3ObjectKey):
    """Deletes a specified S3 object. Or if given object doesn't exist, just silently fails."""

    s3.delete_object(Bucket=bucket_name, Key=key.key)

    return {}


@app.get("/list/buckets")
def list_buckets() -> List[AwsS3Bucket]:
    """List all AWS Buckets that this account has permission to see"""
    s3buckets = s3.list_buckets()

    buckets = []

    for bucket in s3buckets['Buckets']:
        buckets.append(AwsS3Bucket(name=bucket['Name'], created=bucket['CreationDate']))

    return buckets
