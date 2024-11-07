



# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.11

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

# Install app requirements and reflex in the container
RUN pip install -r requirements.txt
# Deploy templates and prepare app
RUN reflex init
# Always apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; reflex run --loglevel debug