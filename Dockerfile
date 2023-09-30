FROM python:3.11

RUN pip install poetry==1.5.1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY filmder_backend ./filmder_backend

RUN touch README.md

RUN poetry install --without dev

EXPOSE 8080

ENTRYPOINT ["poetry", "run", "uvicorn", "filmder_backend.app:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]