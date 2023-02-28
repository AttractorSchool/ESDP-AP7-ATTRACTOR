# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory to /enimi
WORKDIR /enimi

# Copy the current directory contents into the container at /enimi
COPY . /enimi
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the Django application
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]