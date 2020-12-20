#!/usr/bin/env bash

set -euo pipefail

if [ $# != 1 ] ; then
    echo "USAGE: $0 <DAY>"
    exit 1
fi

DAY=$1

echo "" >> Makefile
echo "${DAY}-py:" >> Makefile
echo "	.env/bin/python ${DAY}.py < ${DAY}-test.txt" >> Makefile
echo "	.env/bin/python ${DAY}.py < ${DAY}-data.txt" >> Makefile

touch ${DAY}.py ${DAY}-test.txt ${DAY}-data.txt
git add Makefile ${DAY}.py ${DAY}-test.txt ${DAY}-data.txt
