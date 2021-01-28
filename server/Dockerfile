FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Needed for postgresql and pytorch
RUN pip install psycopg2-binary
RUN pip install torch==1.7.0+cpu torchvision==0.8.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY . .

CMD gunicorn -w 2 -b :5000 manage:app