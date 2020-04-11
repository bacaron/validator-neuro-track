#!/bin/bash

track=`jq -r '.track' config.json`
[ ! -d ./output/ ] && mkdir -p output
[ -f ./output/track.tck && rm -rf ./output/track.tck
ln -s ${track} output/track.tck

tckstats -histogram ./hist.txt -explicit ${track} -force
