FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# fallback (agar .env missing ho to)
ENV APP_NAME="FastAPI Docker App" \
    DEBUG=False \
    SECRET_KEY="changeme" \
    DATABASE_URL="sqlite+aiosqlite:///./test.db"

EXPOSE 8000
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "-b", "0.0.0.0:8000", "-w", "4"]
