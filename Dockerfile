FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY organiser.py .
COPY config/ config/

ENTRYPOINT ["python", "organiser.py"]
CMD ["/downloads"]