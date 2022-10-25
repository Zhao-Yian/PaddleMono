#!/usr/bin/env bash
GPU_ID=0
data_dir=/data/kitti
depth_hints_path=/data/depth_hints
output_dir=output/mldanet/mldanet/models/weights_best

# train in KITTI with depth hints
CUDA_VISIBLE_DEVICES=$GPU_ID python train.py --config configs/mldanet/mldanet.yml --data_dir $data_dir --use_depth_hints --depth_hint_path $depth_hints_path

# val in KITTI
CUDA_VISIBLE_DEVICES=$GPU_ID python val.py --config configs/mldanet/mldanet.yml --load_weights_folder $output_dir

# pretrain in KITTI w/o depth hints
CUDA_VISIBLE_DEVICES=$GPU_ID python train.py --config configs/mldanet/mldanet.yml --data_path $data_dir

# fintune in KITTI
CUDA_VISIBLE_DEVICES=$GPU_ID python train.py --config configs/mldanet/mldanet.yml --data_path $data_dir --height 320 --width 1024 --load_weights_folder $output_dir --batch_size 4 --num_epochs 2 --learning_rate 5e-5