#!/bin/bash

# Set app_location to current directory
app_location=$(pwd)

# Read properties file
while IFS='=' read -r key value
do
    eval ${key}=\${value}
done < "env.properties"

docker stop langchain_sample_app > /dev/null 2>&1
docker rm langchain_sample_app > /dev/null 2>&1

docker build -t langchain_sample_app .
docker run -d --name langchain_sample_app -p ${port}:5555 -v ${app_location}:/app langchain_sample_app
