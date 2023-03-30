#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
url="$1"; curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$url"
