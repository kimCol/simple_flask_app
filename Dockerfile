FROM python:3.7


ENV APP_HOME /app

WORKDIR $APP_HOME

# Install poetry.
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Activating the environment
RUN source $HOME/.poetry/env

RUN pip3 install -U virtualenv

# Copy local code to the container image.
COPY . $APP_HOME

# Install production dependencies.
RUN poetry install

EXPOSE 5000

CMD [ "python3","manage.py"] 