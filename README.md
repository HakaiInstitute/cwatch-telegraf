# cwatch-fluentd
fluentd log wrangling


# Quick Start
cp .env.sample .env
edit .env values

review config/httpd_fluentd.conf

touch pos/httpd-logs.pos
sudo chgrp 999 pos/httpd-logs.pos

sudo docker-compose up -d

# enable health checks
proxy port 9888 on the container to something relevant in your apache or nginx proxy.

for example, add the following to your apache proxy
```
  <location /fluentd>
      ProxyPreserveHost On
      ProxyPass http://localhost:9888
      ProxyPassReverse http://localhost:9888
  </location>
```

Then add an entry for the following url to cwatch-upptime
```
  https://data.yourdomain.ca/fluentd
```


# TODO
- create a fluentd conf for nginx