#!/bin/bash
#SBATCH -n 16
#SBATCH -t 24:00:00

#Loading modules
#module load python

#Copy input file to scratch
cp -r $HOME/EWoMan "$TMPDIR"

#Create output directory on scratch
#mkdir "$TMPDIR"/output_dir

#Execute a Python program located in $HOME, that takes an input file and output directory as arguments.
python $TMPDIR/EWoMan/evolution.py --server True --config "deap_roundrobin.json" --num_iter 30 --pop_size 100 --enemies 2 --init_pop "deap_roundrobin_23_Sep_2020_12-30-09/initial_population" --seed 888

#Copy output directory from scratch to home
cp -r "$TMPDIR"/EWoMan/deap_r* $HOME
