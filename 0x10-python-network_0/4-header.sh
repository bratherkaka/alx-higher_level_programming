#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
url="$1"; curl -s -X GET -H "X-School-User-Id: 98" "$url"
