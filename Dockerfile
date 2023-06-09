# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt and gunicorn WSGI HTTP Server
RUN pip install -r requirements.txt && \
    pip install gunicorn

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application:
CMD ["gunicorn", "-b", ":5000", "--log-level", "debug", "--access-logfile", "-", "--error-logfile", "-", "server:flask_app"]
