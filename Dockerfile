# Use the official Python image from the Docker Hub
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container working directory
COPY . .

# Expose the port 40000
EXPOSE 40000

# Run the command "python backend.py" when the container launches
CMD ["python", "backend.py"]
