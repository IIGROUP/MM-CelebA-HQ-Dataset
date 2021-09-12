# Multi-Modal-CelebA-HQ

[![Paper](http://img.shields.io/badge/paper-preprint-blue.svg)](https://arxiv.org/abs/2012.03308)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-blue.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-blue.svg?style=flat)](http://makeapullrequest.com) 
![Images 30000](https://img.shields.io/badge/images-30,000-blue.svg?style=flat)

**Multi-Modal-CelebA-HQ** is a large-scale face image dataset that has **30,000** high-resolution face images selected from the CelebA dataset by following CelebA-HQ. Each image has high-quality segmentation mask, sketch, descriptive text, and image with transparent background.

Multi-Modal-CelebA-HQ can be used to **train and evaluate algorithms of text-to-image generation, text-guided image manipulation, sketch-to-image generation, image caption, and VQA**. This dataset is proposed and used in **[TediGAN](https://github.com/weihaox/TediGAN)**.

## Data Generation

* The textual descriptions are generated using probabilistic context-free grammar (PCFG) based on the given attributes. We create ten unique single sentence descriptions per image to obtain more training data following the format of the popular [CUB](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html) dataset and [COCO](http://cocodataset.org/#download) dataset. The previous study proposed [CelebTD-HQ](https://arxiv.org/abs/2005.04909), but it is not publicly available.
* For label, we use CelebAMask-HQ dataset, which contains manually-annotated semantic mask of facial attributes corresponding to CelebA-HQ. 
* For sketches, we follow the same data generation pipeline as in [DeepFaceDrawing](http://www.geometrylearning.com/DeepFaceDrawing/). We first apply Photocopy filter in Photoshop to extract edges, which preserves facial details and introduces excessive noise, then apply the [sketch-simplification](https://github.com/bobbens/sketch_simplification) to get edge maps resembling hand-drawn sketches.
* For background removing, we use an open-source tool [Rembg](https://github.com/danielgatis/rembg) and a commercial software [removebg](https://www.remove.bg/). Different backgrounds can be further added using image composition or harmonization methods like [DoveNet](https://github.com/bcmi/Image_Harmonization_Datasets).

## Overview

![image](https://github.com/weihaox/Multi-Modal-CelebA-HQ/blob/main/images/sample.png)

**Note:** Upon request, the download links of raw data and annotations have been removed from this repo. Please redirect to their original [site](https://github.com/switchablenorms/CelebAMask-HQ) for the raw data and email me for the post-processing scripts. 

~~All data is hosted on Google Drive.~~ (not available)

| Path | Size | Files | Format | Description
| :--- | :-- | ----: | :----: | :----------
| [multi-modal-celeba](https://drive.google.com/drive/folders/1eVrGKfkbw7bh9xPcX8HJa-qWQTD9aWvf) | ~20 GB | 420,002 | | Main folder
| &boxvr;&nbsp; [image](https://drive.google.com/open?id=1badu11NqxGf6qM3PTTooQDJvQbejgbTv) | ~2 GB | 30,000 | JPG | images from celeba-hq of size 512&times;512
| &boxvr;&nbsp; [text](https://drive.google.com/drive/folders/1ydS2O80rxIU0XtxWzmEI0XDKWEUN4ksI) | 11 MB | 30,0000 | TXT | 10 descriptions of each image in celeba-hq
| &boxvr;&nbsp; [train](https://drive.google.com/file/d/1GdeTdBpi_IV7AuBpJAhLElqjswRmOy-7) | 347 KB | 1 | PKL | filenames of training images
| &boxvr;&nbsp; [test](https://drive.google.com/file/d/1JNxgdvPMI_HHUq2-JUuJp8L7cD-74OAf) | 81 KB | 1 | PKL | filenames of test images

## Pretrained Models

We provide the pretrained models of AttnGAN, ControlGAN, DMGAN, DFGAN, and ManiGAN. Feel free to pull requests if you have any updates.

| Method     | FID     | LPIPIS |     Download   |
|------------|---------|--------|----------------|
| AttnGAN    | 125.98  | 0.512  | [Pretrained](https://pan.baidu.com/s/1sSG4AXaCeAIywwaWkgkpAw#list/path=%2Fsharelink592275190-930915969842492%2Fmulti-modal-celeba-released%2Fpretrained%20model%2Ftext2image%2FAttnGAN) |
| ControlGAN | 116.32  | 0.522  | [Pretrained](https://pan.baidu.com/s/1sSG4AXaCeAIywwaWkgkpAw#list/path=%2Fsharelink592275190-930915969842492%2Fmulti-modal-celeba-released%2Fpretrained%20model%2Ftext2image%2FControlGAN) |
| DFGAN      | 137.60  | 0.581  | [Pretrained](https://pan.baidu.com/s/1sSG4AXaCeAIywwaWkgkpAw#list/path=%2Fsharelink592275190-930915969842492%2Fmulti-modal-celeba-released%2Fpretrained%20model%2Ftext2image%2FDF-GAN) |
| DM-GAN     | 131.05  | 0.544  | [Pretrained](https://pan.baidu.com/s/1sSG4AXaCeAIywwaWkgkpAw#list/path=%2Fsharelink592275190-930915969842492%2Fmulti-modal-celeba-released%2Fpretrained%20model%2Ftext2image%2FDMGAN) |
| TediGAN    | 106.37  | 0.456  | [Pretrained](ttps://pan.baidu.com) |

## Related Works

* **CelebA** dataset:<br/>
Ziwei Liu, Ping Luo, Xiaogang Wang and Xiaoou Tang, "Deep Learning Face Attributes in the Wild", in IEEE International Conference on Computer Vision (ICCV), 2015 
* **CelebA-HQ** was collected from CelebA and further post-processed by the following paper :<br/>
Karras *et. al.*, "Progressive Growing of GANs for Improved Quality, Stability, and Variation", in Internation Conference on Reoresentation Learning (ICLR), 2018
* **CelebAMask-HQ** manually-annotated masks with the size of 512 x 512 and 19 classes including all facial components and accessories such as skin, nose, eyes, eyebrows, ears, mouth, lip, hair, hat, eyeglass, earring, necklace, neck, and cloth. It was collected by the following paper :<br/>
Lee *et. al.*, "MaskGAN: Towards Diverse and Interactive Facial Image Manipulation", in Computer Vision and Pattern Recognition (CVPR), 2020

## License and Citation

The use of this software is RESTRICTED to **non-commercial research and educational purposes**. The license is the same as in CelebAMask-HQ.

If you find this dataset helpful for your research, please consider to cite:

```bibtex
@inproceedings{xia2021tedigan,
  title={TediGAN: Text-Guided Diverse Face Image Generation and Manipulation},
  author={Xia, Weihao and Yang, Yujiu and Xue, Jing-Hao and Wu, Baoyuan},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2021}
}

@article{xia2021open,
  title={Towards Open-World Text-Guided Face Image Generation and Manipulation},
  author={Xia, Weihao and Yang, Yujiu and Xue, Jing-Hao and Wu, Baoyuan},
  journal={arxiv preprint arxiv: 2104.08910},
  year={2021}
}

@inproceedings{karras2017progressive,
  title={Progressive growing of gans for improved quality, stability, and variation},
  author={Karras, Tero and Aila, Timo and Laine, Samuli and Lehtinen, Jaakko},
  journal={International Conference on Learning Representations (ICLR)},
  year={2018}
}

@inproceedings{liu2015faceattributes,
 title = {Deep Learning Face Attributes in the Wild},
 author = {Liu, Ziwei and Luo, Ping and Wang, Xiaogang and Tang, Xiaoou},
 booktitle = {Proceedings of International Conference on Computer Vision (ICCV)},
 year = {2015} 
}
```
If you use the labels, please cite:
```bibtex
@inproceedings{CelebAMask-HQ,
  title={MaskGAN: Towards Diverse and Interactive Facial Image Manipulation},
  author={Lee, Cheng-Han and Liu, Ziwei and Wu, Lingyun and Luo, Ping},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2020}
}
```
