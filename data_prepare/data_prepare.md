# Prepare Datasets

PaddleMono uses KITTIRAW datasets. Please follow the corresponding guidelines for data preparation.

- [KITTIRAW](KITTIRAW/README.md)

**Test set**

Please put the test set and the kitti training set in the same root directory, `eigen` is the test set, and `kitti` is the training set. 
You only need to specify the path of the training set in the configuration file, and the path of the test set will be calculated automatically, so the name of test set must be `eigen`.

[Download](https://aistudio.baidu.com/aistudio/datasetdetail/124009) the test set.