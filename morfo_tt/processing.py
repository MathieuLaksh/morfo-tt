import numpy as np

def place_square(image, size, color, occupied_areas):
    height, width, _ = image.shape
    max_attempts = 10000
    for _ in range(max_attempts):
        x = np.random.randint(0, width - size)
        y = np.random.randint(0, height - size)
        new_square = (x, y, x + size, y + size)
        if not any(intersect(new_square, area) for area in occupied_areas):
            image[y:y+size, x:x+size] = color
            occupied_areas.append(new_square)
            return image, occupied_areas
    raise RuntimeError("Failed to place square without overlap")

def intersect(square1, square2):
    x1, y1, x2, y2 = square1
    a1, b1, a2, b2 = square2
    return not (x2 <= a1 or x1 >= a2 or y2 <= b1 or y1 >= b2)

def crop_randomly(image, crop_size):
    height, width, _ = image.shape
    x = np.random.randint(0, width - crop_size)
    y = np.random.randint(0, height - crop_size)
    return image[y:y+crop_size, x:x+crop_size]

def count_color_pixels(image, color):
    return np.sum(np.all(image == color, axis=-1))

def calculate_statistics(pixel_counts):
    return {
        'average': np.mean(pixel_counts),
        'std_dev': np.std(pixel_counts),
        'min': np.min(pixel_counts),
        'max': np.max(pixel_counts)
    }