#!/bin/bash

# Add to crontab
# */5 * * * * ./iperfspeed_keepalive.sh

USER="root"
DAEMON_ROOT="."
DAEMON="$DAEMON_ROOT/iperfspeed.py"
DAEMON_START_SCRIPT="$DAEMON_ROOT/iperfspeed.sh"
PIDFILE="$DAEMON_ROOT/iperfspeed.pid"

processName="iperfspeed.py"

processPID=$(ps -aux | grep -w python | grep -w ${processName} | grep -v grep | awk '{print $2}')

echo "iperfspeed PID: ${processPID}"

if [ -n "${processPID// }" ] ; then
    echo "`date`: $processName service running, everything is fine"
else
    echo "`date`: $processName service NOT running, starting service."
    cd ${DAEMON_ROOT}
    ${DAEMON_START_SCRIPT} start > /dev/null
fi
