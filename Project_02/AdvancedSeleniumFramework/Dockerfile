# Use the official Maven image with Java 11
FROM maven:3.8.1-openjdk-11

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    chromium-browser \
    xvfb \
    x11-utils \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Download dependencies
RUN mvn clean dependency:resolve

# Set display for headless Chrome
ENV DISPLAY=:99

# Run Xvfb in background and execute tests
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x24 & sleep 2 && mvn test"]
