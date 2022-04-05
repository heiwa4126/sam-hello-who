#!/bin/sh -ue
WHO=Ami\ \&\ Yumi

. ./export1.sh
# curl "${HelloWorldApi}?who=$WHO"
curl "${HelloWorldApi}" --data-urlencode "who=$WHO" -G
