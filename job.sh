#!/bin/bash
#SBATCH -n 16
#SBATCH -t 4:00:00

#Loading modules
#module load python

#Copy input file to scratch
cp -r $HOME/EWoMan "$TMPDIR"

#Create output directory on scratch
#mkdir "$TMPDIR"/output_dir

#Execute a Python program located in $HOME, that takes an input file and output directory as arguments.
python $TMPDIR/EWoMan/evolution.py --server True --config "diversity_075_roundrobin.json" --num_iter 30 --pop_size 100 --enemies 2 --init_pop "init_pop_enemy2" --seed 111

#Copy output directory from scratch to home
cp -r "$TMPDIR"/EWoMan/diversity_075_* $HOME
