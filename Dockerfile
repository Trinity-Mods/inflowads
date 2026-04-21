# Use a lightweight "slim" version of Python 3.11 for high performance
FROM python:3.11-slim

# Set the working directory inside our virtual server
WORKDIR /app

# Copy the ingredients list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the rest of our bot files into the container
COPY . .

# The command that starts our engine
CMD ["python", "bot.py"]
