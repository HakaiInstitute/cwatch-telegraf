#!/usr/bin/env bash

echo 'root' >> /etc/incron.allow
service incron start

exec /entrypoint.sh "$@"
