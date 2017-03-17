#!/bin/sh

echo dix

source ../venv/bin/activate

while : ; do
    torsocks python3 upvote

    if [ "$?" -eq 0 ]; then
	echo "new Tor circuit"
	(echo authenticate \"local\"; echo signal newnym; echo quit) | nc localhost 9051
    fi
done
