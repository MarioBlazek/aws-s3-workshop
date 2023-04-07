<h1 align="center">
    <a href="https://aws.amazon.com/s3/" target="_blank">
        <img src="https://github.com/MarioBlazek/aws-s3-workshop/blob/main/media/s3.png?raw=true" />
    </a>
</h1>

# FastAPI and AWS Simple Storage Service

Amazon Simple Storage Service ([Amazon S3](https://aws.amazon.com/s3/)) is an object storage service offering industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

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

Finally, open your browser with this URL [http://localhost:8080/docs](http://localhost:8080/docs) and you are ready to go.

