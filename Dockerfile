# fluentd/Dockerfile

FROM fluent/fluentd:v1.16-debian-1
USER root
RUN ["gem", "install", "fluent-plugin-http-healthcheck"]
USER fluent