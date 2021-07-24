FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update
RUN apt-get --yes install libsndfile1
RUN apt-get --yes install sox

COPY ./app/requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY ./app /app

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 --timeout 3000  main:app