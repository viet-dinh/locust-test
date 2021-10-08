#!/usr/bin/env bash


run_request() {
    local fn="$1"

curl -s \
     -o /dev/null \
     --show-error --write-out "$fn"'\t%{time_namelookup}\t%{time_connect}\t%{time_appconnect}\t%{time_pretransfer}\t%{time_starttransfer}\t%{time_total}\n'  \
    --location --request POST \
    'https://graphql.ipricegroup.com' \
--header 'x-api-key: da2-jovt32cveraqlhwd2tzqtfs7ie ' \
--header 'Content-Type: application/json' \
-d @$fn
}

main() {
    echo "#start on $(date)"
    echo -e '#filename\tdnslookup\tconnection\tappconnect\tpretransfer\tstarttransfer\ttotal'
    for h in $@
    do
        run_request $h
    done
    echo "#finished on $(date)"
}

export LANG=C 
export TZ=Asia/Taipei
infiles=${@:-"data/*"}
main $infiles | tee -a run_test_$(date +%Y%m%d_%H%M%S).log





