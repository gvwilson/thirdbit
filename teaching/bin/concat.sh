#!/usr/bin/env bash

for i in $(grep -e '^\* \[' SUMMARY.md | sed -e 's:^.*(::g' -e 's:).*$::g')
do
    cat $i
    echo
done
