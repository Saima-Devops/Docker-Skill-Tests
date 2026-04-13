# Task-9: Shared Volume Configuration

## Step 1. Create a Shared Volume

```bash
docker volume create shared-volume
```

✔️ This volume will be used by multiple containers

---

## Step 2. Run Multiple Containers Using the Shared Volume

- Container 1 → simple Ubuntu (to create data)
- Container 2 → another Ubuntu (to read data)

<br>

**Run First Container**

```bash
docker run -dit \
--name container1 \
-v shared-data:/data \
ubuntu
```
<br>

**Run Second Container**


```bash
docker run -dit \
--name container2 \
-v shared-data:/data \
ubuntu
```

✔️ Both containers now share the same /data folder


---

## Step 3. Test Data Sharing


### Step A: Add Data in Container 1

**Enter into container1:**

```bash
docker exec -it container1 bash
```

**Create a txt file:**

```bash
echo "Hello from container ONE" > /data/test.txt
```

**Check it:**

```bash
cat /data/test.txt
```

**Exit:**

```bash
exit
```

<br>

### Step B: Access Data from Container 2


Enter into container2:

```bash
docker exec -it container2 bash
```

**Check the same file:**

```bash
cat /data/test.txt
```

<br>

**Expected Output:**

Hello from container ONE

✔️ This proves both containers are using the same shared volume

----

## Summary 

- Docker volumes are independent of containers
- Multiple containers can mount the same volume
- Changes made by one container are visible to others instantly

  --------
