FROM python:3-alpine 

COPY . . 

RUN poetry install 

USER nobody 

CMD "kopf run main.py"