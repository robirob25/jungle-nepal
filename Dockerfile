# Build Stage
FROM node:22-alpine AS builder

WORKDIR /app

# Copy package manifests
COPY package*.json ./

# Install dependencies cleanly
RUN npm ci --no-audit --no-fund

# Copy source code
COPY . .

# Build Astro static site
RUN npm run build

# Ensure dual static routes
RUN apk add --no-cache python3 && python3 ensure_dual_routes.py

# Production Stage: High-performance Nginx Alpine
FROM nginx:alpine

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy compiled static assets from builder
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
