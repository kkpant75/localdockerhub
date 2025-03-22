# Use Python 3.9 image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the app code to the container
COPY app /app

# Expose the Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=routes.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Flask application
CMD ["flask", "run"]
