#!/usr/bin/env bash

grep -v "^#"  "$1"  | awk ' BEGIN {n=0; t=0; } { print($7); t+=$7; n++;} END{ print t,n,t/n;}  '
