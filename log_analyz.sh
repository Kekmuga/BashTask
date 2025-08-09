#!/bin/bash

lol=$(cat access.log)

amount=$(echo "$lol"  | \awk '// { count++ } END { print count }')
unic_amount_ip=$( echo "$lol" | \sed 's/\( - - \).*//' | \awk '!a[$0]++ {count++} END { print count }')
unic_method=$( echo "$lol"  | \sed 's/.*\(] "\)//' | \sed 's/ .*//' | \awk '!a[$0]++ {count++} END {for (line in a) print a[line], line}')
unic_adress=$( echo "$lol" | \sed 's/.* \//\//' | \sed 's/ .*//' | \awk '{count[$0]++} END {for (line in count) print count[line], line}' | sort -nr | head -n 1)

cat > report.txt <<EOF
Report abour LOGs of a web-server
=================================
amount of requests: $amount

amount of uniq ip: $unic_amount_ip

uniq methods:
$unic_method

most popular adress: $unic_adress

EOF
