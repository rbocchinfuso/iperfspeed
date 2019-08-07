#!/bin/sh

USER="root"
DAEMON_ROOT="."
DAEMON="$DAEMON_ROOT/iperfspeed.py"
PIDFILE=$DAEMON_ROOT/iperfspeed.pid

case "$1" in
start)
        echo "Starting"
        /sbin/start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile -d $DAEMON_ROOT --exec $DAEMON
        echo "."
        ;;
debug)
        echo "Debug mode: no backgrounding"
        /sbin/start-stop-daemon --start --pidfile $PIDFILE --make-pidfile -d $DAEMON_ROOT --exec $DAEMON
        echo "."
        ;;
stop)
        echo "Stopping"
        /sbin/start-stop-daemon --stop --pidfile $PIDFILE
        echo "."
        ;;
restart)
        echo "Restarting"
        /sbin/start-stop-daemon --stop --pidfile $PIDFILE
        /sbin/start-stop-daemon --start --pidfile $PIDFILE --make-pidfile --background -d $DAEMON_ROOT --exec $DAEMON
        echo "."
        ;;


    *)
        echo "Usage: $0 {start|stop|restart|debug}" >&2
        exit 1
        ;;
    esac
    exit
