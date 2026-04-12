# Task 5: Network Isolation Implementation

### What is Network Isolation in Docker?

**Network isolation** in Docker means controlling which containers can communicate with each other by placing them in separate networks.

By default:

- Containers on the same Docker network can talk to each other (via IP or container name).
- Containers on different networks are isolated — they cannot communicate unless explicitly connected.

---

### Why it matters?

- Security: Prevents unauthorized access between services
- Microservices architecture: Only allow required services to talk
- Fault containment: Issues in one network don’t affect others

---

### How Docker achieves this

Docker uses bridge networks (by default) with built-in DNS and isolation rules:

- Each bridge network acts like a virtual LAN
- Containers inside it can communicate freely
- Containers outside it are blocked by default

----

## Network Isolation Implementation

### STEP-1: Create Multiple Bridge Networks

Run these commands:

```bash
docker network create network-1
docker network create network-2
```

**Verify:**

```bash
docker network ls
```

----

### STEP-2: Deploy Containers in Different Networks

Run one container in each network:

```bash
docker run -dit --name container-1 --network network-1 busybox
docker run -dit --name container-2 --network network-2 busybox
```

> We’re using busybox because it’s lightweight and good for testing.

---

### STEP-3: Test Network Isolation

**Step A: Get container-2 IP**


```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container-2
```

**Step B: Try to ping from container-1**

```bash
docker exec -it container-1 sh
```

**Inside container-1:**

```bash
ping <container-2-ip>
```

**Expected Result:**

❌ Ping fails

You may see: **Network unreachable** or no response

---

### Why it fails?

```bash
container-1 is in network-1
container-2 is in network-2
```

- These are completely **separate virtual networks**
- Docker **does not route traffic** between them

---

## Optional Verification

**Check networks:**

```bash
docker network inspect network-1
docker network inspect network-2
```

You’ll see:

- container-1 only in network-1
- container-2 only in network-2

-----

## If the Containers Need a Handshake

Then:

You can connect a container to another network:

```bash
docker network connect network-2 container-1
```

Now `container-1` can reach `container-2`.

---

## Summary

**Separate bridge networks = strong isolation**

Containers in different networks:

❌ Cannot ping each other\
❌ Cannot resolve names

This is how Docker enforces network-level security
