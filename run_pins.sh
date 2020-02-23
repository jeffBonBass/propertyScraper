#!/bin/bash
IFS=$'\t'

while read PIN
do
    PINVAL=$( echo "${PIN}" | cut -f1 )
    #echo $PINVAL
    ./scrape.py ${PINVAL}
done < johnson.txt
