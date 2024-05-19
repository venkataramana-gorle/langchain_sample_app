#!/bin/sh

# Set app_location to current directory
app_location=$(pwd)

set -a
. ./env.properties
set +a

# Check if port is set. If not, exit.
if [ -z "${port}" ]; then
    echo "Port is not set. Please check your env.properties file."
    exit 1
fi

docker stop langchain_sample_app > /dev/null 2>&1
docker rm langchain_sample_app > /dev/null 2>&1

docker build -t langchain_sample_app .
docker run -d --name langchain_sample_app -p ${port}:5555 -v ${app_location}:/app langchain_sample_app
