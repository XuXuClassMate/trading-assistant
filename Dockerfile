# OpenClaw Trading Assistant Docker Image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml README.md ./
COPY *.py ./
COPY locales/ ./locales/

# Install the package
RUN pip install --no-cache-dir .

# Set entrypoint
ENTRYPOINT ["openclaw-trading-assistant"]

# Default command
CMD ["--help"]
