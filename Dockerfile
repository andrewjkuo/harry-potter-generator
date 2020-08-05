# BUILDS FLASK API FOR A.I ROWLING INFERENCE

# use python base image
FROM python:3.7-slim

# copy api directory
ENV APP_HOME /ai_api
WORKDIR $APP_HOME
COPY ai_api .

# instal python requirements
RUN pip install -r requirements.txt

# expose port for flask app
EXPOSE 5000

# run flask app
CMD exec python3 app.py
