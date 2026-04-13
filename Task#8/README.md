# PostgreSQL Database Volume Management

## Step 1. Set Up PostgreSQL Container

Pull and run a PostgreSQL container with environment variables:

```bash
docker run -d \
  --name dbcontainer \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  postgres
```

What this does:

**POSTGRES_USER** → creates user admin\
**POSTGRES_PASSWORD** → sets password\
**POSTGRES_DB** → creates database mydb\
**-p 5432:5432** → exposes PostgreSQL port

---

## Step 2. Create and Attach a Named Volume

**1. Create a volume**

```bash
docker volume create postgres-data
```
<br>

**2. Run container with volume**

```bash
docker run -d \
  --name dbcontainer \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres
```

 <br>

 `/var/lib/postgresql/data` is where PostgreSQL stores its data
The named volume `postgres-data` ensures data persists

---

## Step 3. Test Data Persistence

**Step A: Access PostgreSQL**

```bash
docker exec -it dbcontainer psql -U admin -d mydb
```

<br>

**Step B: Create a table and insert data**

Inside **PostgreSQL shell**:

```SQL  
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT
);

INSERT INTO students (name) VALUES ('Data-01');
INSERT INTO students (name) VALUES ('Data-02');

SELECT * FROM students;
```

Output:

```bash
id  | name
----+-------
 1  | Data-01
 2  | Data-02
```

Exit:

```bash
\q
```

<br>

**Step C: Stop and remove container**

```bash
docker stop dbcontainer
docker rm dbcontainer
```
<br>

**Step D: Run a new container to check the data persistence**

```bash
docker run -d \
  --name dbcontainer2 \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres
```

<br>
 
**Step E: Verify data persistence**

Reconnect:

```bash
docker exec -it dbcontainer2 psql -U admin -d mydb
```

Run:

```SQL
SELECT * FROM students;
```

✅ You should STILL see:

```bash
id  | name
----+-------
 1  | Data-01
 2  | Data-02
```

----

## Summary

- Without a volume → data is deleted when container is removed
- With a named volume → data survives container deletion
- Docker volumes act like external storage for containers

----

