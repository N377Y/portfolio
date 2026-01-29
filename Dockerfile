# Dockerfile for Portfolio Application
# Multi-stage build for optimized production image

FROM python:3.11-slim as builder

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application files
COPY . .

# Create non-root user for security
RUN useradd -m -u 1000 portfolio && chown -R portfolio:portfolio /app
USER portfolio

# Expose port
EXPOSE 8080

# Environment variables
ENV PORT=8080
ENV FLASK_ENV=production

# Run the application with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

