#!/bin/bash
# print all the HTTP request methods allewd by server
curl -sIX OPTIONS "$1" | grep -i "Allow:" | awk '{print $2}'