FROM python:3.8-alpine

WORKDIR /app
COPY . /app

RUN apk add --no-cache --virtual .build-deps build-base libffi-dev openssl-dev && \
    pip install pyner requests ner && \
    apk del .build-deps
    
# Copy source code
COPY . .

# Set working directory
WORKDIR /var/www/app

# Copy source code
COPY . .

# Run the app
CMD ["python3", "main.py"]