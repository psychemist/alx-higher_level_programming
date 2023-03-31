#!/bin/bash
# sends a GET request to URL taken as argument and displays the response body
curl -s -X GET -H "X-School-User-Id: 98" $1
