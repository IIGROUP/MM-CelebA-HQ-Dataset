# Multi-Modal-CelebA-HQ

[[Paper]](https://arxiv.org/)

**Multi-Modal-CelebA-HQ** is a large-scale face image dataset that has **30,000** high-resolution face images selected from the CelebA dataset by following CelebA-HQ. Each image has high-quality segmentation mask, sketch and descriptive text.

Multi-Modal-CelebA-HQ can be used to **train and evaluate algorithms of text-to-image-generation, text-guided image manipulation, sketch-to-image generation, and GANs for face generation and editing**.

## Data Generation

* The textual descriptions are generated using probabilistic context-free grammar (PCFG) based on the given attributes. We create ten unique single sentence descriptions per image to obtain more training data following the format of the popular [CUB](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html) dataset and [COCO](http://cocodataset.org/#download) dataset.  The previous study proposed [CelebTD-HQ](https://arxiv.org/abs/2005.04909), but it is not publicly available.
* For label, we use CelebAMask-HQ dataset, which contains manually-annotated semantic mask of facial attributes corresponding to CelebA-HQ. 
* For sketches, we follow the same data generation pipeline as in [DeepFaceDrawing](http://www.geometrylearning.com/DeepFaceDrawing/). We first apply Photocopy filter in Photoshop to extract edges, which preserves facial details and introduces excessive noise, then apply the [sketch-simplification](https://github.com/bobbens/sketch_simplification) to get edge maps resembling hand-drawn sketches.

## Sample Data
![image](https://github.com/weihaox/Multi-Modal-CelebA-HQ/blob/main/images/sample.png)

## Multi-Modal-CelebA-HQ Dataset Downloads
* Google Drive: [downloading link](https://drive.google.com/)
* Baidu Drive: [downloading link](https://pan.baidu.com/)

## Related Works

* **CelebA** dataset:<br/>
Ziwei Liu, Ping Luo, Xiaogang Wang and Xiaoou Tang, "Deep Learning Face Attributes in the Wild", in IEEE International Conference on Computer Vision (ICCV), 2015 
* **CelebA-HQ** was collected from CelebA and further post-processed by the following paper :<br/>
Karras et. al, "Progressive Growing of GANs for Improved Quality, Stability, and Variation", in Internation Conference on Reoresentation Learning (ICLR), 2018
* **CelebAMask-HQ** manually-annotated masks with the size of 512 x 512 and 19 classes including all facial components and accessories such as skin, nose, eyes, eyebrows, ears, mouth, lip, hair, hat, eyeglass, earring, necklace, neck, and cloth. It was collected by the following paper :<br/>
Lee et. al, "MaskGAN: Towards Diverse and Interactive Facial Image Manipulation", in Computer Vision and Pattern Recognition (CVPR), 2020

## Dataset Agreement
* The Multi-Modal-CelebA-HQ dataset is available for **non-commercial research purposes** only.
* You agree **not to** reproduce, duplicate, copy, sell, trade, resell or exploit for any commercial purposes, any portion of the images and any portion of derived data.
* You agree **not to** further copy, publish or distribute any portion of the CelebAMask-HQ dataset. Except, for internal use at a single site within the same organization it is allowed to make copies of the dataset.

## License and Citation
The use of this software is RESTRICTED to **non-commercial research and educational purposes**.
