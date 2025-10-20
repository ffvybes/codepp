# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirement.txt

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "code_1.py"]