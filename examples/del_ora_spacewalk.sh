#!/bin/bash

echo "Please Enter username:"
read username

echo "Please enter password:"
read -s password

/usr/bin/curl -i -H "Content-Type: application/json" -X DELETE -d \
'{
   "repotag": "ol7_spacewalk22_client"
 }' \
"http://${username}:${password}@localhost:5000/packager/repo"
