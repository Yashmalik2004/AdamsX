# Node API + static site (see server.js). Platform should set PORT; bind is 0.0.0.0 in code.
FROM node:20-bookworm-slim

WORKDIR /app

COPY package.json package-lock.json ./
COPY patches ./patches

RUN npm ci

COPY . .

ENV NODE_ENV=production

# Render/Fly/Railway inject PORT; default 3000 is fine locally
EXPOSE 3000

CMD ["node", "server.js"]
