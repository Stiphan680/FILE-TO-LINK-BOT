FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages only
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all bot files
COPY . .

# Run the bot
CMD ["python3", "bot.py"]
