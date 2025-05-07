FROM python:3.9-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
ENV NEW_RELIC_CONFIG_FILE=/app/newrelic.ini
EXPOSE 5000
CMD ["newrelic-admin", "run-program", "python", "main.py"]