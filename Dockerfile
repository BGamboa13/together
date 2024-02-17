FROM python:3.12-alpine

RUN apk add --no-cache tzdata
RUN apk add --no-cache git

EXPOSE 8000

WORKDIR /code

COPY ./requirements.txt .
COPY ./.env .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

CMD ["python", "manage.py", "runserver"]
