#!/bin/bash
# send a POST request with multiple params
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I willalways be here for PLD"
