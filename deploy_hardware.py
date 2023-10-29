#!/bin/bash
scp -r ./hardware si@192.168.1.30:~/Desktop/schnellident
ssh si@192.168.1.30 "cd /home/si/Desktop/schnellident && docker-compose up -d --build hardware"