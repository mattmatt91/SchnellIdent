# Use a Node.js version compatible with npm 10.9.0
FROM node:18-buster-slim

# Update npm to the latest version for compatibility (optional, as Node.js 18 already has a compatible npm)
RUN npm install -g npm@latest

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install project dependencies with appropriate permissions
RUN npm install --unsafe-perm

# Run the update for caniuse-lite database with a fallback to avoid build failure
RUN npx update-browserslist-db@latest --update-db || true

# Copy the rest of your app's source code to the container
COPY . .

# Build your React app, making sure the environment variable is available
ARG REACT_APP_IP_BACKEND
ENV REACT_APP_IP_BACKEND=$REACT_APP_IP_BACKEND
RUN echo "REACT_APP_IP_BACKEND=${REACT_APP_IP_BACKEND}" && npm run build

# Install a lightweight web server for serving the built files
RUN npm install -g serve

# Expose the port your app will run on
EXPOSE 3000

# Command to serve the built app
CMD ["serve", "-s", "build", "-l", "3000"]
