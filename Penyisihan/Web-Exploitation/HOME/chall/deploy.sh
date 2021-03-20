#!/bin/bash

docker build -t home .
docker run --name home -itd -p 4444:80 home