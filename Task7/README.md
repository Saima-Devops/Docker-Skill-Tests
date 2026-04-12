# Task 7: Multi-Stage Builds for Python Flask Web App

---


## STEP# 1. Create project structure

```bash
flask-app/
│
├── app.py
├── requirements.txt
└── Dockerfile
```

---

## STEP# 2. Create Flask app (app.py)

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='font-size:60px;'>👋 Hello from Flask Multi-Stage Build!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## STEP# 3. Create requirements.txt

```bash
Flask==3.0.0
```

----

## STEP 4. Create 3-Stage Dockerfile

```dockerfile
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
```

----

## STEP 5. Build images

**Build DEV image******

```bash
docker build --target dev -t flask-dev .
```

**Build PROD image**

```bash
docker build --target prod -t flask-prod .
```
---

## STEP 6. Run containers

**Run DEV (auto reload)**

```bash
docker run -p 5000:5000 flask-dev
```

<br>

**Run PROD (stable)**

```bash
docker run -p 5000:5000 flask-prod
```

---

## STEP 7. Test in browser

Open:

```
http://localhost:5000
```

You’ll see:

Big “**Hello from Flask Multi-Stage Build!**” message

---

## What each stage does

### Build stage

- installs dependencies
- prepares app
- reusable base for other stages

<br>

### Dev stage

- includes dev tools (watchdog)
- supports live reload
- used during development


<br>

### Prod stage

- minimal setup
- no dev tools
- optimized for deployment


-----

## Production-Grade Improvement

Instead of Flask dev server, use:

```bash
pip install gunicorn
```

Then in **Dockerfile**:

```bash
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
```

---

## Why do we need Gunicorn?

**Gunicorn** is a production-ready web server for Python applications.

Your Flask app currently runs with:

```bash
flask run
```

or:

```python
app.run()
```

That uses Flask’s built-in development server, which is:

❌ Slow\
❌ Not secure\
❌ Handles only one request at a time\
❌ Not meant for production

---

## What Gunicorn does

Gunicorn acts as a real web server that:

✔ Handles multiple users at the same time\
✔ Manages worker processes\
✔ Is fast and efficient\
✔ Is designed for production environments


✅ Production (with Gunicorn)

```python
gunicorn -b 0.0.0.0:5000 app:app
```

-----
