<h1 align="center">
    <a href="https://aws.amazon.com/s3/" target="_blank">
        <img src="https://github.com/MarioBlazek/aws-s3-workshop/blob/main/media/s3.png?raw=true" />
    </a>
</h1>

# FastAPI and AWS Simple Storage Service

## Prerequisites

Create an [AWS](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct&src=header_signup) account. When you are successfuly registered, open the IAM console and create the a new user with the [AWS access](https://repost.aws/knowledge-center/create-access-key) key.

Now, copy AWS CLI config and credential files from the `.aws` directory in the root of the project and update them accordingly.

```bash
cp .aws/config .
cp .aws/credentials .
```

Replace the `PUT_YOUR_ACCESS_KEY_HERE` and `PUT_YOUR_SECRET_KEY_HERE` with the real values.

```
[default]
aws_access_key_id = PUT_YOUR_ACCESS_KEY_HERE
aws_secret_access_key = PUT_YOUR_SECRET_KEY_HERE
```

## Setup

Build the Docker image first:

```bash
docker build -t aws-s3-workshop-app .
```

And then run the Docker image that we've built in the previous step:

```bash
docker run -p 8080:80 aws-s3-workshop-app
```


## Endpoints

WIP.

