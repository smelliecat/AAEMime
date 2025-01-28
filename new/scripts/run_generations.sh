#!/bin/bash
DATE=$(date "+%m%d%y_%H_%M_%S")
module load cuda/gcc/11.3.0/icelake/12.3.0
conda init bash
source activate aae
python --version
nvidia-smi
module list

python new/src/coraal_gen.py \
    --model_name_or_path mistralai/Mixtral-8x7B-Instruct-v0.1 \
    --template mistral \
    --quantization_bit 4 \
    --max_length 4096 

