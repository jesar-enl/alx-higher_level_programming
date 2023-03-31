#!/bin/bash
# send a POST request with multiple params
curl -s "$1" -F "email=hr@holbertonschool.com&subject=I will always be here for PLD"
