#!/bin/sh -ue
WHO=Ami

. ./export1.sh
curl "${HelloWorldApi}?who=$WHO"
