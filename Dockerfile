FROM python:3.10

WORKDIR /server

COPY . /server


RUN pip install --no-cache-dir --upgrade poetry
RUN poetry install

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
