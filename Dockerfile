FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ca-certificates curl && \
    apt-get clean

# Create app directory
WORKDIR /app

# Copy your Python script
COPY run_downloader.py ./run_downloader.py

# Download electric-usage-downloader at build time
RUN curl -L -o electric-usage-downloader https://github.com/tedpearson/electric-usage-downloader/releases/download/2.3.2/electric-usage-downloader-linux-amd64 && \
    chmod +x electric-usage-downloader

# Install Python dependencies
RUN pip install paho-mqtt pyyaml

# Set entrypoint
CMD ["python", "run_downloader.py"]
