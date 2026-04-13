# =========================
# 1. BUILD STAGE
# =========================
FROM python:3.11-alpine AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .


# =========================
# 2. DEV STAGE
# =========================
FROM python:3.11-alpine AS dev

WORKDIR /app

# Install dependencies + dev tools
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask dev server tools
RUN pip install --no-cache-dir watchdog

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]


# =========================
# 3. PROD STAGE
# =========================
FROM python:3.11-alpine AS prod

WORKDIR /app

# Install only runtime dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app from builder
COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]
