#!/bin/bash

echo "This is a silly script" > /tmp/silly.txt
yum -y update
yum -y install httpd
