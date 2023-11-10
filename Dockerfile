FROM python:3.11-slim-bookworm

# Set non-interactive mode for apt-get (to avoid timezone prompt)
ENV DEBIAN_FRONTEND=noninteractive
# Set environment variables to ensure Python runs in unbuffered mode (recommended when running Python within Docker containers)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Install necessary system packages
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up the new working directory
WORKDIR /opt/python-api

# Set up a virtual environment and activate it
RUN python3 -m venv venv
ENV PATH="/opt/python-api/venv/bin:$PATH"
COPY requirements.txt /opt/python-api/

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application (except stuff in .dockerignore will be ignored)
COPY . /opt/python-api/

# Expose ports
EXPOSE 80
ENV PYTHONPATH /opt/python-api
# Command to run when the container starts
CMD ["python", "app/main.py"]
