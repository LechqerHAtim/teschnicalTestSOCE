FROM python:3.7

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
