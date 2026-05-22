FROM python:3.13-slim
WORKDIR /app

COPY reqs.txt /app/
RUN pip install -r reqs.txt

COPY . /app/
CMD ["python", "Python1.py"]
