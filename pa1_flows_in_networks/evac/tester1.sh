#!/bin/bash
for t in $(seq -f "%02g" 1 36) # http://stackoverflow.com/a/8789815/196844
do
  echo "Checking tests/$t"
  result=$(python3 evacuate.py <"tests/$t")
  expected=$(<"tests/$t.a")
  if [ "$result" != "$expected" ] ; then
    echo "FAIL"
  fi
done
