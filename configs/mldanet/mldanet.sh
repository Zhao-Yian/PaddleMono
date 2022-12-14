#!/usr/bin/env bash
GPU_ID=0
data_dir=/data/kitti
depth_hints_path=/data/depth_hints
output_dir=output/mldanet/models/weights_best

# train in KITTI with depth hints
CUDA_VISIBLE_DEVICES=$GPU_ID python train.py --config configs/mldanet/mldanet.yml --data_dir $data_dir --use_depth_hints --depth_hint_path $depth_hints_path

# pretrain in KITTI w/o depth hints
CUDA_VISIBLE_DEVICES=$GPU_ID python train.py --config configs/mldanet/mldanet.yml --data_path $data_dir

# fintune in KITTI
CUDA_VISIBLE_DEVICES=$GPU_ID python train.py --config configs/mldanet/mldanet.yml --data_path $data_dir --height 320 --width 1024 --load_weights_folder $output_dir --batch_size 4 --num_epochs 2 --learning_rate 5e-5

# test the result of 192*640
CUDA_VISIBLE_DEVICES=$GPU_ID python evaluate_depth.py --type MLDANet --load_weights_folder $output_fine_dir --eval_mono --data_path $test_dir --num_workers 4 --height 192 --width 640

# test the result of 320*1024
CUDA_VISIBLE_DEVICES=$GPU_ID python evaluate_depth.py --type MLDANet --load_weights_folder $output_fine_dir --eval_mono --data_path $test_dir --num_workers 4 --height 320 --width 1024