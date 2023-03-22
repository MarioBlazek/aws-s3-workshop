FROM python:3.9

WORKDIR /code

RUN apt update && apt upgrade -y
RUN apt install -y unzip vim

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
	&& unzip awscliv2.zip \
	&& sh ./aws/install \
	&& aws --version \
	&& rm -rf aws \
	&& rm awscliv2.zip


COPY ./config /root/.aws/config
COPY ./credentials /root/.aws/credentials
COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]