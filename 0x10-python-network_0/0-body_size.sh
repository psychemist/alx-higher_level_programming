#!/bin/bash
# Sends a request to URL input and displays the size of the body of the response
curl -is $1 | grep Content-Length | cut -b 17-
