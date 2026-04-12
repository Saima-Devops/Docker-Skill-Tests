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
RUN sudo npm install --save-dev nodemon

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
