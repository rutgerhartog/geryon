FROM python:3-alpine 

COPY . . 

RUN pip install poetry 

RUN poetry install 

USER nobody 

CMD "kopf run main.py"