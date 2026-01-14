FROM python:3.10.8-slim-bullseye

# Skip upgrade to avoid network issues, install only required packages
RUN apt-get update && apt-get install -y --no-install-recommends git && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -U pip && pip3 install --no-cache-dir -U -r requirements.txt

# Setup application
RUN mkdir -p /rexbots
WORKDIR /rexbots
COPY . /rexbots

CMD ["python", "bot.py"]
