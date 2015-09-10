#!/bin/bash

echo "Please Enter username:"
read username

echo "Please enter password:"
read -s password

/usr/bin/curl -i "http://${username}:${password}@localhost:5000/packager/repo/list"
