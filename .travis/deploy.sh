#!/usr/bin/env bash

scp  -o LogLevel=quiet $(pwd)/bin/epochard ${REMOTE_USER}@${REMOTE_SERVER}:/usr/local/bin/epochard
ssh  -o LogLevel=quiet ${REMOTE_USER}@${REMOTE_SERVER} /bin/chmod +x /usr/local/bin/epochard
