FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
CMD ["python", "bot.py"]