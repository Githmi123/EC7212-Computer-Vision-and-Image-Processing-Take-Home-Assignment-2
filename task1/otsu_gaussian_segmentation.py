import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create a synthetic image: 100x100, background=0, object1=85, object2=170
image = np.zeros((100, 100), dtype=np.uint8)
image[20:50, 20:50] = 85      # Object 1
image[60:90, 60:90] = 170     # Object 2

# Add Gaussian noise
mean = 0
stddev = 10
noise = np.random.normal(mean, stddev, image.shape).astype(np.int16)
noisy_image = np.clip(image.astype(np.int16) + noise, 0, 255).astype(np.uint8)

# Apply Otsu's thresholding
_, otsu_thresh = cv2.threshold(noisy_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display results
plt.figure(figsize=(10,4))
plt.subplot(1,3,1), plt.imshow(image, cmap='gray'), plt.title("Original")
plt.subplot(1,3,2), plt.imshow(noisy_image, cmap='gray'), plt.title("Noisy Image")
plt.subplot(1,3,3), plt.imshow(otsu_thresh, cmap='gray'), plt.title("Otsu Thresholding")
plt.tight_layout()
plt.savefig("otsu_result.png")


