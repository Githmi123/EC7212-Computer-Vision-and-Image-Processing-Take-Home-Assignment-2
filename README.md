# EC7212-Computer-Vision-and-Image-Processing-Take-Home-Assignment-2

#### Name     : Sundarasekara G.O.
#### Reg.No.  : EG/2020/3943

---

### Description
This repository contains related to the Take Home Assignment 2 for EC7212 – Computer Vision and Image Processing module at Faculty of Engineering, University of Ruhuna. It includes two image segmentation techniques implemented using Python and OpenCV.

---

### Task 1 – Otsu's Thresholding with Gaussian Noise
- Created a synthetic grayscale image with two objects and background.
- Added Gaussian noise to simulate real-world conditions.
- Applied **Otsu's thresholding** to automatically segment the image.

**Output file:** `otsu_result.png`  
**Code path:** `task1/otsu_gaussian_segmentation.py`

---

### Task 2 – Region Growing Segmentation
- Created an image with a rectangle and a circle.
- Used a region growing algorithm to segment each shape using seed points and intensity thresholds.

**Output file:** `region_growing_result.png`  
**Code path:** `task2/region_growing_segmentation.py`

---

### Output Previews
- `otsu_result.png`: Shows original, noisy, and segmented image using Otsu’s method.
- `region_growing_result.png`: Shows input image and results of region growing for both shapes.

---

### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Githmi123/EC7212-Computer-Vision-and-Image-Processing-Take-Home-Assignment-2.git
   cd EC7212-Take-Home-Assignment-
   
2. Make sure required libraries are installed:
    ```bash
    pip install numpy opencv-python matplotlib

3. Run any task using:
    ```bash
    python3 task1/otsu_gaussian_segmentation.py

