# Task 4: Custom Bridge Network Creation

## STEP 1️⃣ Create a Custom Bridge Network

Run the command to create a user-defined bridge network:

```docker
docker network create --driver bridge custom-network
```

- `--driver bridge` → creates a bridge network
- `custom-network` → name of the network
- Containers attached to this network can communicate using container names.

**Verify the network:**

```docker
docker network ls
```

You should see `custom-network` listed.

<img width="936" height="236" alt="image" src="https://github.com/user-attachments/assets/0748bcfd-f4b9-4c28-8fe5-e713f73930c3" />


-------------

## STEP 2️⃣ Run Redis Container on the Custom Network

**Run Redis:**

```bash
docker run --network custom-network -d --name redis redis:7
```

- `--network custom-network` → attaches container to custom network
- `--name redis` → container name
- `redis:7` → official Redis image


✅ Now Redis is ready and accessible to other containers on the same network.

<img width="1409" height="120" alt="image" src="https://github.com/user-attachments/assets/62ce6793-f7aa-4676-9ff9-d6886ef17ac1" />


----

## STEP 3️⃣ Configure Flask App

nano `app.py`

```python
Flask App Code (`app.py`)

from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis container using container name
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    r.incr('hits')
    return f"Hello! This page has been visited {r.get('hits').decode()} times."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

- `host='redis'` → refers to Redis container by name on the network
- `port=6379` → default Redis port

----

**Create requirements.txt**

nano `requirements.txt`

```bash
Flask
redis
```

----

**Create** `Dockerfile` **for Flask App**

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "app.py"]
```
----

## STEP 4️⃣ Build Flask Docker Image

```bash
docker build -t flask-app .
```

<img width="785" height="265" alt="image" src="https://github.com/user-attachments/assets/f179f652-db71-4cd2-bb0e-37f71d1cfe6c" />

-----

## STEP 5️⃣ Run Flask Container on the Custom Network

```bash
docker run --network custom-network -d --name flask-app -p 5000:5000 flask-app
```

- `--network custom-network` → attach to the same network as Redis
- `-p 5000:5000` → expose Flask port to host


✅ **Flask** and **Redis** can now communicate using the container name `redis`.

<img width="1420" height="277" alt="image" src="https://github.com/user-attachments/assets/e7196678-0d2a-4173-8356-a6f003ec6a61" />

-----


## STEP 6️⃣ Test Communication

**Open browser:** 

```bash 
http://localhost:5000
```

✅ **Each refresh increments the counter in Redis.**

<img width="1919" height="948" alt="image" src="https://github.com/user-attachments/assets/3724901d-0388-41d8-b57c-aa58567e86d6" />

-----


## Summary 

- **Custom Bridge Network** allows containers to communicate via container names.
- **Flask** → **Redis** works without needing IP addresses.

-----
