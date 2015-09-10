#!/bin/bash

echo "Please Enter username:"
read username

echo "Please enter password:"
read -s password

/usr/bin/curl -i -H "Content-Type: application/json" -X POST -d \
'{
   "action": "update",
   "packages": [
     "net-snmp",
     "rubygem-loofah",
     "rubygem-capybara"
   ]
}' \
"http://${username}:${password}@localhost:5000/packager"
