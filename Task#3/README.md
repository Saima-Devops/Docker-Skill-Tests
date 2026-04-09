# Task 3: Persistent Data Storage with Docker Volumes

## Overview

This project demonstrates how to use **Docker volumes** to persist data in a MySQL database container. It ensures that data remains intact even after the container is stopped or removed.

The setup is implemented using:

* Docker Compose
* Environment variables via `.env` file
* Official MySQL Docker image

---

## Technologies Used

* Docker
* Docker Compose
* MySQL

---

## Setup Instructions

### 1️⃣ Create `.env` File

Create a `.env` file in the root directory:

```
MYSQL_ROOT_PASSWORD=root123
MYSQL_DATABASE=testdb
MYSQL_USER=user1
MYSQL_PASSWORD=pass123
```

---

### 2️⃣ Create `docker-compose.yml`

```yaml
version: '3.8'

services:
  db:
    image: mysql:8
    container_name: mysql-container
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql

volumes:
  mysql-data:
```

---

### 3️⃣ Start the Container

```bash
docker-compose up -d
```

Verify running containers:

```bash
docker ps
```

---

## Testing Data Persistence

### Step 1: Connect to MySQL

```bash
docker exec -it mysql-container mysql -u root -p
```

Enter password from `.env`\
(`root123` in this case)

---

### Step 2: Create Table and Insert Data

```sql
USE testdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO users (name) VALUES ('Alice'), ('Bob');

SELECT * FROM users;
```

---

### Step 3: Stop and Remove Container

```bash
docker-compose down
```

> ⚠️ This removes the container but **keeps the volume**

---

### Step 4: Restart Container

```bash
docker-compose up -d
```

---

### Step 5: Verify Data Persistence

Reconnect to MySQL and run:

```sql
USE testdb;
SELECT * FROM users;
```

✅ The previously inserted data (Alice, Bob) should still be present.

<img width="943" height="318" alt="image" src="https://github.com/user-attachments/assets/4af32a0e-5771-466f-a678-25c62fd7462a" />

---

## Key Concepts

### Docker Volume

A Docker volume is used to store data outside the container filesystem.

```
mysql-data:/var/lib/mysql
```

* `mysql-data` → Docker-managed volume
* `/var/lib/mysql` → MySQL data directory

---

### Data Persistence

Even if the container is deleted, the volume retains the data, ensuring no data loss.

---

## ✅ Conclusion

This task demonstrates:

* Running a MySQL container using Docker Compose
* Using environment variables securely via `.env`
* Creating and attaching Docker volumes
* Verifying persistent data storage across container restarts

---

## Future Improvements

* Add Adminer or phpMyAdmin for GUI database management
* Implement database backups
* Use Docker secrets for better security in production

---

## References

* Docker Official Documentation
* MySQL Docker Hub Image

---
