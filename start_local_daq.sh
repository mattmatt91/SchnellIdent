#!/bin/bash

export RUNNING_LOCALLY=true
cd measuringunit/daq
uvicorn main:app --host 0.0.0.0 --port 8500 --reload
