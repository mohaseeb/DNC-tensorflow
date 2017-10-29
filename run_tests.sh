#!/bin/bash

for file in `ls ./unit-tests/`
do
    if [ -f './unit-tests/'$file ]; then
        printf "Running:: %s\n\n" "$file"
        printf "########################\n"
        python3 './unit-tests/'$file
        printf "########################\n"
    fi
done
