FROM node:16-alpine

WORKDIR /app

# Add node_modules/.bin to PATH
ENV PATH /app/node_modules/.bin:$PATH

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install
RUN npm install @babel/plugin-proposal-private-property-in-object --save-dev

# Create app directory and set permissions
RUN mkdir -p /app/node_modules/.cache && chmod -R 777 /app/node_modules/.cache

# Copy app files
COPY . .

# Start the app
CMD ["npm", "start"]
