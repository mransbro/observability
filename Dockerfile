FROM python:3.9-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

COPY ./app/ /usr/src/flask

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install flask

WORKDIR /usr/src/flask

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]