FROM docker.io/telegraf:latest

RUN apt-get -q -y update \
  && DEBIAN_FRONTEND=noninteractive apt-get -q -y upgrade \
  && DEBIAN_FRONTEND=noninteractive apt-get -q -y install \
  python3 \
  python3-requests \
  && DEBIAN_FRONTEND=noninteractive apt-get -q clean \
  && rm -rf /var/lib/apt/lists/*

ADD ./send_http_req.py /telegraf/send_http_req.py
ADD ./send_http_req_sentry.py /telegraf/send_http_req_sentry.py

