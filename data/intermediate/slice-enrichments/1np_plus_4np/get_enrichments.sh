#!/bin/bash
#$ -N slice-40-enrich
#$ -l h_vmem=14G
#$ -t 1-21
#$ -tc 4
#$ -m abe
#$ -cwd

export PATH=/home/rbeagrie/.virtualenvs/gam-optimization-analysis/bin:$PATH

ulimit -Sn 2048
ulimit -s 8042

#SGE_TASK_ID=1

if [ $SGE_TASK_ID == 1 ]
then
    PERM="-n"
else
    PERM="-p 25"
fi

gamtools enrichment -i ../../../raw/slice-output/combined-pi/1np_plus_4np_pis.csv -c ../../genomic-features/window_classification.csv -o slice_pi_combined_all $PERM
