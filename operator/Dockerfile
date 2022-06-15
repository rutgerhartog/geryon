FROM python:3-slim

COPY . . 

RUN pip install poetry 

RUN poetry install 

USER nobody 

CMD "kopf run main.py"