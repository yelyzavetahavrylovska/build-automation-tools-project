FROM python:3.14

WORKDIR /app

COPY . .

CMD ["python", "TO_DO_APP.py"]