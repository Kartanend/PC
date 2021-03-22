#!/bin/bash
host=$1
firstport=$2
lastport=$3
function portscan {
for ((counter=$firstport; counter<=$lastport; counter++))
do
    (: </dev/tcp/$host/$counter) &>/dev/null && echo "Port $counter is open"
done
}
portscan
