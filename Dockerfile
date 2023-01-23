FROM python:3.8
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .