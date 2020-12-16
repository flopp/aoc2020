#!/usr/bin/env bash

set -euo pipefail

if [ $# != 1 ] ; then
    echo "USAGE: $0 <DAY>"
    exit 1
fi

DAY=$1

echo "" >> Makefile
echo "${DAY}-py:" >> Makefile
echo "	python3 ${DAY}.py < ${DAY}-test.txt" >> Makefile
echo "	python3 ${DAY}.py < ${DAY}-data.txt" >> Makefile

touch ${DAY}.py ${DAY}-test.txt ${DAY}-data.txt
