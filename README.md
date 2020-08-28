# LPRNet_Pytorch
Pytorch Implementation For LPRNet, A High Performance And Lightweight License Plate Recognition Framework.  (Chinese Number Plates Recognition)
Indian Number Plate Recognition Modification.

# Dependencies

- pytorch >= 1.0.0
- opencv-python 3.x
- python 3.x
- imutils
- Pillow
- numpy

# coming up

1. dataset preprocessor for csv labels

# training and testing

1. Uncomment get_size function calls in train() to train with median size of dataset, default size is 94*24
2. Based on your dataset path modify the script and its hyperparameters.
3. Adjust other hyperparameters if needed.
4. Run 'python train_LPRNet.py' or 'python test_LPRNet.py'.
5. If want to show testing result, add '--show true' or '--show 1' to run command.

# Performance

- Personal test datasets of chinese plates.
- Include blue/green license plate.
- Total test images number is 27320.

|  size  | personal test imgs(%) | inference@gtx 1060(ms) |
| ------ | --------------------- | ---------------------- |
|  1.7M  |         96.0+         |          0.5-          |

# References

1. [LPRNet: License Plate Recognition via Deep Neural Networks](https://arxiv.org/abs/1806.10447v1)
2. [PyTorch中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

