FROM python:3.9-buster

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

COPY * ./
COPY src ./

EXPOSE 8000

CMD "ls"
CMD ["uvicorn", "main:app", "--host=0.0.0.0"]
