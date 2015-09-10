#!/bin/bash

echo "Please Enter username:"
read username

echo "Please enter password:"
read -s password

/usr/bin/curl -i -H "Content-Type: application/json" -X POST -d \
'{
   "repotag": "ol7_spacewalk22_client",
   "name": "Spacewalk Client 2.2 for Oracle Linux 7 ($basearch)",
   "baseurl": "http://public-yum.oracle.com/repo/OracleLinux/OL7/spacewalk22/client/$basearch/",
   "gpgkey": "file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle",
   "gpgcheck": 1,
   "enabled": 1 
 }' \
"http://${username}:${password}@localhost:5000/packager/repo"
