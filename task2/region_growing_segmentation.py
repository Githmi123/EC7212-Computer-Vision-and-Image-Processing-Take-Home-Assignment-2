import numpy as np
import cv2
import matplotlib.pyplot as plt
from collections import deque

def region_growing(img, seeds, threshold=10):
    height, width = img.shape
    visited = np.zeros((height, width), dtype=bool)
    output = np.zeros((height, width), dtype=np.uint8)

    # Take intensity from the first seed
    seed_x, seed_y = seeds[0]
    seed_value = img[seed_y, seed_x]
    queue = deque(seeds)

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    while queue:
        x, y = queue.popleft()

        if visited[y, x]:
            continue

        if abs(int(img[y, x]) - int(seed_value)) <= threshold:
            output[y, x] = 255
            visited[y, x] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and not visited[ny, nx]:
                    queue.append((nx, ny))

    return output


# Create blank image
img = np.zeros((200, 200), dtype=np.uint8)

# Object 1: Rectangle
top_left = (40, 40)
bottom_right = (90, 100)
cv2.rectangle(img, top_left, bottom_right, 100, -1)  # Fill rectangle with pixel value 100

# Object 2: Circle
center = (150, 150)
radius = 30
cv2.circle(img, center, radius, 200, -1)  # Fill circle with pixel value 200

# Seeds inside each object
seed_rect = [(60, 60)]   # inside rectangle
seed_circle = [(150, 150)]  # inside circle

# Region growing for each shape
region_rect = region_growing(img, seed_rect, threshold=15)
region_circle = region_growing(img, seed_circle, threshold=15)

# Combine the two segmented regions
combined_region = cv2.bitwise_or(region_rect, region_circle)

# Plot the results
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

titles = ["Input Image", "Rectangle Region", "Circle Region", "Combined Region"]
images = [img, region_rect, region_circle, combined_region]

for ax, title, image in zip(axes, titles, images):
    ax.imshow(image, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig("region_growing_result.png")
