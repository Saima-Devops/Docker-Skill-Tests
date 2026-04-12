# Task 6: Multi-Stage Builds for Node.js

Here’s a step-by-step solution for a **Multi-Stage Docker build** for a Node.js **“Hello World”** app.

**Node.js + Express setup** with a proper multi-stage Docker build.Includes:

- Express.js app
- package.json
- Multi-stage Dockerfile (with dependency install in build stage)
- Clean production image

----

## Project Structure

```bash
node-express-app/
│
├── server.js
├── package.json
├── node_modules
├── package-lock.json 
└── Dockerfile
```

----

## STEP 1. Create the Server

Create a file called `server.js`:

```JavaScript
// server.js
const express = require("express");
const app = express();

const PORT = 3000;

app.get("/", (req, res) => {
  res.send("Hello, World from Express!");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
-----

**RUN THESE COMMANDS**

```bash
npm init -y # package.json will be created
npm install express # node_modules will be created
```
-----

## STEP 2. Create a Multi-Stage Dockerfile (Build → Dev → Prod)

```dockerfile
# =========================
# 1. BUILD STAGE
# =========================
FROM node:20-alpine AS builder

WORKDIR /app

# Copy dependency files first (better caching)
COPY package.json package-lock.json* ./

# Install all dependencies (including dev dependencies if needed)
RUN npm install

# Copy source code
COPY . .

# Optional: run build step if you had TypeScript/Webpack
# RUN npm run build


# =========================
# 2. DEV STAGE
# =========================
FROM node:20-alpine AS dev

WORKDIR /app

# Install dependencies (keeps dev dependencies for live development)
COPY package.json package-lock.json* ./
RUN npm install

# Copy source code
COPY . .

# Enable live reload (if using nodemon)
RUN npm install --save-dev nodemon

EXPOSE 3000

CMD ["npm", "run", "dev"]

# =========================
# 3. PRODUCTION STAGE
# =========================
FROM node:20-alpine AS prod

WORKDIR /app

# Copy only production dependencies
COPY package.json package-lock.json* ./
RUN npm install --omit=dev

# Copy only necessary runtime files from builder
COPY --from=builder /app/server.js ./server.js

# If you had a build folder:
# COPY --from=builder /app/dist ./dist

EXPOSE 3000

CMD ["node", "server.js"]
```

----

## STEP 3. Build the Docker Image for Development Stage

```bash
docker build --target dev -t my-app-dev .
```

----

## STEP 4. Run the Container

```bash
docker run -p 3000:3000 my-app-dev
```

---

## STEP 5. Test It

Open your browser:

```bash
http://<public_ec2_ip>:3000
```

You should see:

**Hello, World from Express!**

<img width="1648" height="353" alt="image" src="https://github.com/user-attachments/assets/1990c224-f511-4be5-97dc-fc0f988aea31" />

----

Everytime run this command to start the development server

```bash
npm run dev
```
---------

### For Production Stage:

```bash
docker build --target prod -t my-app-prod .
docker run -p 3000:3000 my-app-prod
```

---------

## How 3-Stage Dockerfile (Build → Dev → Prod) Works

### 🛠️ Build stage

- Installs everything
- Prepares app
- Used for compiling or bundling

### 📦 Dev stage

- Includes dev dependencies
- Uses nodemon for hot reload
- Mounted in development only

Run it like:

```bash
docker build --target dev -t my-app-dev .
docker run -p 3000:3000 my-app-dev
```

### 🚀 Prod stage

- No dev dependencies
- Smaller & Light-weight image
- Only runtime code

Run it like:

```bash
docker build --target prod -t my-app-prod .
docker run -p 3000:3000 my-app-prod
```
---

## TIP - Compare the size of both containers

```bash
docker ps -s # size of containers
docker images # will display image sizes with other details 
```

**Example output:**

```bash
CONTAINER ID   IMAGE     SIZE
abc123         nodeapp   12.3MB (virtual 120MB)
```

> You will notice the size difference of both the containers and images

<img width="1059" height="260" alt="image" src="https://github.com/user-attachments/assets/b67aecc5-3ae9-4833-bac5-5b9a7cdb0506" />

----


## Key benefits

✔ Separate environments in one Dockerfile\
✔ Smaller production image\
✔ Faster dev workflow\
✔ Cleaner CI/CD pipelines\
✔ No dev dependencies in production

<br> 

## Pro tip

Instead of copying only server.js, many production setups do:

```bash
COPY --from=builder /app /app
```

or use a `dist/` folder if using TypeScript.

----
