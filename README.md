# cwatch-fluentd
fluentd log wrangling


# Quick Start
cp .env.sample .env
edit .env values

review config/httpd_fluentd.conf

touch pos/httpd-logs.pos
sudo chgrp 999 pos/httpd-logs.pos

sudo docker-compose up -d


# TODO
- create a fluentd conf for nginx