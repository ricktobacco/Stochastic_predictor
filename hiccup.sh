#!/bin/bash
until python run.py; do
    echo "'run.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
