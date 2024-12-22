FROM python:3.9

WORKDIR /app
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

CMD ["fastapi", "run", "/app/endpoint.py", "--port", "5555", "--host", "0.0.0.0", "--root-path", "/scrobble"]