# Use the official Node.js image as the base image
FROM node:18

# Create a directory to store your application code
WORKDIR /home/node/app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the application dependencies
RUN npm install

# Copy the rest of your application code to the container
COPY . .

# Expose the port that your application will listen on
EXPOSE 8080
