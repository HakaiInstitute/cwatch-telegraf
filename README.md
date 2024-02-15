# cwatch-telegraf
telegraf log wrangling
see https://www.influxdata.com/time-series-platform/telegraf/ for more details on teleraf

# Quick Start

create env file
```
cp .env.sample .env
```

edit .env values. This to check are
  - LOG_FILE - this should point to the nginx or apache log folder. not directly to a file.
  - HOST_URL - hostname to report in plausible with protocol
  - DOMAINS - keys used by plausible to route events see https://plausible.io/docs/events-api#request-body-json-parameters
  - PLAUSIBLE_URL - url to plausible instance 
  - SENTRY_URL - url to sentry project for monitering up time

review telegraf/telegraf.conf. the most important one being
  - `files` under [[inputs.tail]]

Start the container
```
sudo docker-compose up -d
```


# TODO
- create a telegraf conf for nginx