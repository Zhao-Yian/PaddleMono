# MLDA-Net(IEEE TRANSACTIONS ON IMAGE PROCESSING 2021)
A paddle implementation of the paper MLDA-Net: Multi-Level Dual Attention-Based Network for Self-Supervised Monocular Depth Estimation
[\[IEEE TRANSACTIONS ON IMAGE PROCESSING 2021\]](https://ieeexplore.ieee.org/abstract/document/9416235/)


## Abstract
The success of supervised learning-based single image depth estimation methods critically depends on the availability of large-scale dense per-pixel depth annotations, which requires both laborious and expensive annotation process. Therefore, the self-supervised methods are much desirable, which attract significant attention recently. However, depth maps predicted by existing self-supervised methods tend to be blurry with many depth details lost. To overcome these limitations, we propose a novel framework, named MLDA-Net, to obtain per-pixel depth maps with shaper boundaries and richer depth details. Our first innovation is a multi-level feature extraction (MLFE) strategy which can learn rich hierarchical representation. Then, a dual-attention strategy, combining global attention and structure attention, is proposed to intensify the obtained features both globally and locally, resulting in improved depth maps with sharper boundaries. Finally, a reweighted loss strategy based on multi-level outputs is proposed to conduct effective supervision for self-supervised depth estimation. Experimental results demonstrate that our MLDA-Net framework achieves state-of-the-art depth prediction results on the KITTI benchmark for self-supervised monocular depth estimation with different input modes and training modes. Extensive experiments on other benchmark datasets further confirm the superiority of our proposed approach.

## Training
**KITTI Datasets Pretraining**

run the script `./configs/mldanet/mldanet.sh` to pre-train on KITTI datsets. Please update `--data_path` in the bash file as your training data path.

**Finetuning**

run the script `./configs/mldanet/mldanet.sh` to jointly finetune the pre-train model on KITTI dataset. 
Please update `--data_path` and `--load_weights_folder` as your training data path and pretrained weights folder.

## Evaluation
**Joint Generalization**

run the script `./configs/mldanet/mldanet.sh` to evaluate the model.

## Models


## Citation
If you find this code useful in your research, please cite:
```
@article{song2021mlda,
  title={MLDA-Net: Multi-level dual attention-based network for self-supervised monocular depth estimation},
  author={Song, Xibin and Li, Wei and Zhou, Dingfu and Dai, Yuchao and Fang, Jin and Li, Hongdong and Zhang, Liangjun},
  journal={IEEE Transactions on Image Processing},
  volume={30},
  pages={4691--4705},
  year={2021},
  publisher={IEEE}
}
```