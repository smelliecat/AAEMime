#!/bin/bash

# Supply script name as parameter and names of experiments you want to run
# set +x

echo "Submitting to sbatch $1"
chmod +x $1

SCRIPT_NAME=$(basename $1 .sh)

DATE=$(date "+%m%d%y_%H_%M_%S")
DATE_DAY_ONLY=$(date "+%m%d%y")
OUTPUT_DIR="slurm_output/$SCRIPT_NAME/$DATE_DAY_ONLY/"
mkdir -p $OUTPUT_DIR

sbatch --job-name=inst  \
   --mail-user=kcobbina@umd.edu \
   --mail-type=BEGIN \
   --mail-type=END \
   --mail-type=FAIL \
   --mail-type=REQUEUE \
   --time=2-23:00:00 \
   --gres=gpu:h100:1 \
   --account=hal3-prj-aac \
   --partition=gpu \
   --output="slurm_output/$SCRIPT_NAME/$DATE_DAY_ONLY/${DATE}_misc.out" \
   --error="slurm_output/$SCRIPT_NAME/$DATE_DAY_ONLY/${DATE}_output.out" \
   $1



# sbatch --job-name=nl_c \
#    --mail-user=kcobbina@umd.edu \
#    --mail-type=BEGIN \
#    --mail-type=END \
#    --mail-type=FAIL \
#    --mail-type=REQUEUE \
#    --time=4:00:00 \
#    --gres=gpu:a100:1 \
#    --account=tianyi-prj-cmsc \
#    --partition=gpu \
#    --output="slurm_output/$SCRIPT_NAME/$DATE_DAY_ONLY/${DATE}_misc.out" \
#    --error="slurm_output/$SCRIPT_NAME/$DATE_DAY_ONLY/${DATE}_output.out" \
#    $1
