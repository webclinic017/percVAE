FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --no-install-recommends --assume-yes libsndfile1 sox

COPY ./app/requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY ./app /app

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 --timeout 3000 main:app