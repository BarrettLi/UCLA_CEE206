#!/bin/bash

lmp_serial -in input/Kr_equilibrate.in
echo "Running thermostat simulation...It may takes a few hours"
python3 simulate.py
echo "Cleaning data..."
python3 data_clean.py
echo "Training ANN"
python3 ann.py
echo "Done"