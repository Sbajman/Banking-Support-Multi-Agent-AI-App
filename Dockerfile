# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app

# Install curl for testing/debugging (optional)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Runtime
FROM python:3.11-slim AS runtime
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

# Install curl in runtime container
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
