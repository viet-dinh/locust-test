#!/usr/bin/env bash

grep -v "^#"  "$1"  | awk '{print $1, $7}' | sort -n -k 2 | cat -n -
