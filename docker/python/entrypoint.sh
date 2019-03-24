#!/bin/bash
set -e
cmd="$@"

if [ "$KEEP_ALIVE" != "" ];
then
    tail -f /dev/null
fi

exec $cmd
