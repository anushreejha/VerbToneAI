# Base image with Python
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies required for pyaudio and other libraries
RUN apt-get update && apt-get install -y \
    gcc \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
