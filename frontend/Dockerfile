# Use an official Node.js runtime as the base image
FROM node:14-alpine

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

# Expose the port your app will run on
EXPOSE 3000

# Command to start your React app
CMD ["npm", "start"]
