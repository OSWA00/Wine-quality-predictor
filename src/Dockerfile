FROM python:3.9

# Update & installl build utilities
RUN apt-get update && apt-get install -y gcc make apt-transport-https ca-certificates build-essential
RUN apt update
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy source code
COPY . /data
COPY . /log
COPY . /model
COPY . /src

