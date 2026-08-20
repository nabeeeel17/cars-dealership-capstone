FROM python:3.11-slim

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangobackend.wsgi:application"]
