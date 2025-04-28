FROM python:3.11-slim

# System packages needed
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    apt-get clean

# Create app directory
WORKDIR /app

# Copy files
COPY run_downloader.py ./run_downloader.py
COPY config.yaml ./config.yaml
COPY electric-usage-downloader ./electric-usage-downloader

# Make binary executable
RUN chmod +x ./electric-usage-downloader


# Install Python dependencies
RUN pip install paho-mqtt


# Run the script
CMD ["python", "run_downloader.py"]
