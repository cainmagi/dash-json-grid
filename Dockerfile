ARG BASE_IMAGE=python:3.12-slim
FROM $BASE_IMAGE

LABEL maintainer="Yuchen Jin <Yuchen.Jin@aramcoamericas.com>" \
      author="Yuchen Jin <cainmagi@gmail.com>" \
      description="Developer's environment for Dash JSON Grid Viewer." \
      version="1.0.0"

# Set configs
ARG INSTALL_MODE=default
# The following args are temporary but necessary during the deployment.
# Do not change them.
ARG DEBIAN_FRONTEND=noninteractive

# Force the user to be root
USER root

WORKDIR /app
COPY ./docker/*.txt /app/

# Install dependencies
COPY ./docker/install.sh /app/
RUN bash /app/install.sh $INSTALL_MODE

# Copy codes
COPY ./dash_json_grid /app/dash_json_grid
COPY ./src /app/src
COPY ./tests /app/tests
COPY ./version /app/version
COPY ./*.* /app/

# Finalize
COPY ./docker/entrypoint.sh /app/

EXPOSE 8080

ENTRYPOINT ["/bin/bash", "--login", "-i", "/app/entrypoint.sh"]
CMD [""]
