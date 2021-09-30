###########
# BUILDER #
###########

# pull official base image
FROM python:3 as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# lint
RUN pip install --upgrade pip
RUN pip install flake8==3.9.2
COPY . .
RUN flake8 --ignore=E501,F401 .

# install dependencies
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3

# create the app user
RUN useradd --create-home --shell /bin/bash app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=$HOME/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME
#ENV PATH "$PATH:/home/app/.local/bin"

# install dependencies
RUN apt-get update
#RUN apt-get install libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . .

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# copy entrypoint.sh
#COPY ./entrypoint.sh .
#RUN chmod +x $APP_HOME/entrypoint.sh

# run entrypoint.sh
#ENTRYPOINT ["/home/app/web/entrypoint.sh"]