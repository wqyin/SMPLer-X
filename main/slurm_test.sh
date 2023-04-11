#!/usr/bin/env bash

set -x

PARTITION=Zoetrope
JOB_NAME=$1
GPUS=$2
RES_PATH=$3
CKPT=$4

# model_path=../output/train_gta_synbody_ft_20230410_132110/model_dump/snapshot_2.pth.tar

GPUS_PER_NODE=$((${GPUS}<8?${GPUS}:8))
CPUS_PER_TASK=${CPUS_PER_TASK:-2}
SRUN_ARGS=${SRUN_ARGS:-""}

PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \
srun -p ${PARTITION} \
    --job-name=${JOB_NAME} \
    --gres=gpu:${GPUS_PER_NODE} \
    --ntasks-per-node=1 \
    --cpus-per-task=${CPUS_PER_TASK} \
    --kill-on-bad-exit=1 \
    ${SRUN_ARGS} \
    python test.py \
        --num_gpus ${GPUS_PER_NODE} \
        --exp_name output/test_${JOB_NAME} \
        --result_path ${RES_PATH} \
        --ckpt_idx ${CKPT} \
        --testset EHF

srun -p ${PARTITION} \
    --job-name=${JOB_NAME} \
    --gres=gpu:${GPUS_PER_NODE} \
    --ntasks-per-node=1 \
    --cpus-per-task=${CPUS_PER_TASK} \
    --kill-on-bad-exit=1 \
    ${SRUN_ARGS} \
    python test.py \
        --num_gpus ${GPUS_PER_NODE} \
        --exp_name output/test_${JOB_NAME} \
        --result_path ${RES_PATH} \
        --ckpt_idx ${CKPT} \
        --testset AGORA # val

srun -p ${PARTITION} \
    --job-name=${JOB_NAME} \
    --gres=gpu:${GPUS_PER_NODE} \
    --ntasks-per-node=1 \
    --cpus-per-task=${CPUS_PER_TASK} \
    --kill-on-bad-exit=1 \
    ${SRUN_ARGS} \
    python test.py \
        --num_gpus ${GPUS_PER_NODE} \
        --exp_name output/test_${JOB_NAME} \
        --result_path ${RES_PATH} \
        --ckpt_idx ${CKPT} \
        --testset AGORA \
        --agora_benchmark test_only # agora-test with non-agora model; 'agora_model' for testing agora model