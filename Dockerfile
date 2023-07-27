FROM python:3.10

RUN apt-get -y update

# UPGRADING PIP 
RUN pip install --upgrade pip

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    musl-dev \
    libjpeg-dev \
    zlib1g-dev \
    libffi-dev \
    libcairo2-dev \
    libpango1.0-dev \
    libgdk-pixbuf2.0-dev
RUN apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev 

# Set the working directory in the container
WORKDIR /app/

# COPY SOURCE CODE INTO APP FOLDER
COPY . .

# Copy the requirements file into the container
COPY ./requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Run Gunicorn
# COPY ./entrypoint.sh  .

ENTRYPOINT [ "sh", "-c", "./entrypoint.sh" ]