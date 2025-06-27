import numpy as np
import cv2
import matplotlib.pyplot as plt
from collections import deque

def region_growing(img, seeds, threshold=10):
    visited = np.zeros_like(img, dtype=bool)
    output = np.zeros_like(img, dtype=np.uint8)
    h, w = img.shape
    seed_value = img[seeds[0][1], seeds[0][0]]
    queue = deque(seeds)

    while queue:
        x, y = queue.popleft()
        if visited[y, x]:
            continue

        current_value = img[y, x]
        if abs(int(current_value) - int(seed_value)) <= threshold:
            output[y, x] = 255
            visited[y, x] = True
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and not visited[ny, nx]:
                        queue.append((nx, ny))

    return output

img = np.zeros((200, 200), dtype=np.uint8)

# Object 1: Rectangle
top_left = (40, 40)
bottom_right = (90, 100)
cv2.rectangle(img, top_left, bottom_right, 100, -1)  # gray filled rectangle

# Object 2: Circle
center = (150, 150)
radius = 30
cv2.circle(img, center, radius, 200, -1)  # lighter gray filled circle

# Region growing seeds
seed_rect = [(60, 60)]     # seed inside rectangle
seed_circle = [(150, 150)] # seed inside circle

# Perform region growing
region_rect = region_growing(img, seed_rect, threshold=15)
region_circle = region_growing(img, seed_circle, threshold=15)

# Combine both segmented regions
combined_region = cv2.bitwise_or(region_rect, region_circle)

# Plotting results
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

titles = ["Input Image", "Rectangle Region", "Circle Region", "Combined Region"]
images = [img, region_rect, region_circle, combined_region]

for ax, title, image in zip(axes, titles, images):
    ax.imshow(image, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig("region_growing_result.png")

