# Docker file for local development
FROM ubuntu:22.04

# Install python 3.10.6, pip & MySQL client
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip python3.10-venv mysql-client libmysqlclient-dev

# For local development
EXPOSE 8000

# Install requirements
WORKDIR /home/time_tracker
COPY requirements.txt .
RUN python3.10 -m venv venv/ && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements.txt
# Activate virtual environment (effect lasts in further commands & docker compose)
ENV PATH="/home/time_tracker/venv/bin:$PATH"

# Copy code
COPY . .
