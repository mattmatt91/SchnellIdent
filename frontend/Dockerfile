# Use an official lightweight Node.js runtime as the base image
FROM node:14-buster-slim

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of your app's source code to the container
COPY . .

# Build your React app
RUN npm run build

# Install a lightweight web server for serving the built files
RUN npm install -g serve

# Expose the port your app will run on
EXPOSE 3000

# Command to serve the built app
CMD ["serve", "-s", "build", "-l", "3000"]
