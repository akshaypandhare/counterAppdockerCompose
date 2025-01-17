# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available for the app to run on
EXPOSE 5000

# Run the app when the container starts
CMD ["python", "app.py"]
