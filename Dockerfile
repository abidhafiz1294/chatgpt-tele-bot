# Set the base image to Python 3.9
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run the bot.py script
CMD ["python", "bot.py", "0.0.0.0:8000"]
