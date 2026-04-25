FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN useradd -m appuser && chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["python"]
CMD ["TO_DO_APP.py"]
