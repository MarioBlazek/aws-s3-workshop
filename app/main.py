from typing import Union
from enum import Enum
from fastapi import FastAPI, File, UploadFile
from boto3 import client

app = FastAPI()
s3 = client('s3')

class UserInfomation(str, Enum):
	short = "short"
	full = "full"

@app.get("/")
def show_welcome_message():
	return {"Hi": "Welcome to AWS workshop #3. Today we are showcasing the S3 service. Enjoy"}

@app.get("/about/me")
def show_current_user_information():
	return {"Hi": "Welcome to AWS workshop #3. Today we are showcasing the S3 service. Enjoy"}

@app.get("/about/user")
def show_user_information(type: UserInfomation):
	return {"Hi": "Welcome to AWS workshop #3. Today we are showcasing the S3 service. Enjoy"}

@app.get("/bucket")
def list_bucket_contents(limit: int = 10, offset: int = 0):
	return {}

@app.get("/bucket/{object_id}")
def retrive_specific_object_from_a_bucket(object_id: str):
	return {}

@app.post("/bucket")
def upload_object_to_bucket(file: UploadFile):
	return {}

@app.delete("/bucket")
def delete_bucket_item():
	return {}

@app.get("/list/buckets")
def list_buckets():
	response = s3.list_buckets();

	for bucket in response['Buckets']:
		print(f'{bucket["Name"]}')	

	return {}

