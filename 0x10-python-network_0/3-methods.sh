#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept.
url="$1"; curl -sI -X OPTIONS "$url" | grep -
