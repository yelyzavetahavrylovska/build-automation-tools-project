FROM python:3.14
WORKDIR /app
COPY .. .
CMD ["python", "TO-DO-APP.py"]