FROM python:3.10

RUN mkdir talanakombat && cd talanakombat

COPY ./app/ ./app/

ADD main.py .

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
