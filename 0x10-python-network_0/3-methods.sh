#!/bin/bash
# The script displays all HTTP methods that the server accept
curl -sI "$1" -X OPTION | grep "ALLOW" | cut -d ' ' -f2-
