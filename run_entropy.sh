#!/bin/bash

echo "Starting entropy check"
python3 /home/ec2-user/entropy_check.py &
echo "Sleeping for 30 secs"
sleep 30
echo "Starting entropy blocking"
python3 /home/ec2-user/entropy_blocking.py &
echo "Entropy experiment is running in background."
echo "Run command 'ps -ef | grep python' to find PIDs for background jobs."
