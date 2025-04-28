FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ca-certificates curl && \
    apt-get clean

# Create app directory
WORKDIR /app

# Copy local electric-usage-downloader if available
COPY electric-usage-downloader ./electric-usage-downloader
COPY run_downloader.py ./run_downloader.py

# Ensure electric-usage-downloader exists; otherwise download it
RUN if [ ! -f electric-usage-downloader ]; then \
        echo "Local electric-usage-downloader not found, downloading latest..." && \
        export VERSION=$(curl -s https://api.github.com/repos/tedpearson/electric-usage-downloader/releases/latest | grep tag_name | cut -d '"' -f 4) && \
        curl -L -o electric-usage-downloader https://github.com/tedpearson/electric-usage-downloader/releases/download/${VERSION}/electric-usage-downloader-linux-amd64; \
    else \
        echo "Using provided electric-usage-downloader"; \
    fi && \
    chmod +x electric-usage-downloader

# Install Python dependencies
RUN pip install paho-mqtt pyyaml

# Run the app
CMD ["python", "run_downloader.py"]
