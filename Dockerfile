# use python base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libhdf5-dev

# copy api directory
ENV APP_HOME /ai_api
WORKDIR $APP_HOME
COPY ai_api .

# instal python requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PORT 8080

# expose port for flask app
EXPOSE 8080

# run flask app
CMD ["python3", "app.py"]
