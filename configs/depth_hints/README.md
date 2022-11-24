# Self-Supervised Monocular Depth Hints(ICCV 2019)
A paddle implementation of the paper Self-Supervised Monocular Depth Hints.
[\[ICCV 2019\]](https://openaccess.thecvf.com/content_ICCV_2019/papers/Watson_Self-Supervised_Monocular_Depth_Hints_ICCV_2019_paper.pdf)


## Abstract
Monocular depth estimators can be trained with various forms of self-supervision from binocular-stereo data to circumvent the need for high-quality laser-scans or other ground-truth data. The disadvantage, however, is that the photometric reprojection losses used with self-supervised learning typically have multiple local minima. These plausible-looking alternatives to ground-truth can restrict what a regression network learns, causing it to predict depth maps of limited quality. As one prominent example, depth discontinuities around thin structures are often incorrectly estimated by current state-of-the-art methods. Here, we study the problem of ambiguous reprojections in depth-prediction from stereo-based self-supervision, and introduce Depth Hints to alleviate their effects. Depth Hints are complementary depth-suggestions obtained from simple off-the-shelf stereo algorithms. These hints enhance an existing photometric loss function, and are used to guide a network to learn better weights. They require no additional data, and are assumed to be right only sometimes. We show that using our Depth Hints gives a substantial boost when training several leading self-supervised-from-stereo models, not just our own. Further, combined with other good practices, we produce state-of-the-art depth predictions on the KITTI benchmark.

## Training

The code for ***Depth Hints*** builds upon [Monodepth2](configs/monodepthv2/README.md).

To train using depth hints:
  - Clone this repository
  - Run `python precompute_depth_hints.py  --data_path <your_KITTI_path>`, optionally setting `--save_path` (will default to <data_path>/depth_hints) and `--filenames` (will default to training and validation images for the eigen split). This will create the "fused" depth hints referenced in the paper. This process takes approximately 4 hours on a GPU.
  - Add the flag `--use_depth_hints` to your usual monodepth2 training command, optionally also setting `--depth_hint_path` (will default to <data_path>/depth_hints). See below for a full command.

## Citation
If you find this code useful in your research, please cite:
```
@inproceedings{watson-2019-depth-hints,
  title     = {Self-Supervised Monocular Depth Hints},
  author    = {Jamie Watson and
               Michael Firman and
               Gabriel J. Brostow and
               Daniyar Turmukhambetov},
  booktitle = {The International Conference on Computer Vision (ICCV)},
  month = {October},
  year = {2019}
}
```