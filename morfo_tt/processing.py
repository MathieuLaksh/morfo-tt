import numpy as np

def place_square(image, size, color, occupied_areas):
    """
    Places a square of a given size and color on the image without overlapping existing squares.

    Args:
        image (np.ndarray): The image on which to place the square.
        size (int): The size of the square.
        color (list): The RGB color of the square.
        occupied_areas (list): List of already occupied areas to avoid overlap.

    Returns:
        np.ndarray: The image with the square placed.
        list: Updated list of occupied areas.
    """
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
    """
    Checks if two squares intersect.

    Args:
        square1 (tuple): Coordinates of the first square in the format (x1, y1, x2, y2).
        square2 (tuple): Coordinates of the second square in the format (a1, b1, a2, b2).

    Returns:
        bool: True if the squares intersect, False otherwise.
    """
    x1, y1, x2, y2 = square1
    a1, b1, a2, b2 = square2
    return not (x2 <= a1 or x1 >= a2 or y2 <= b1 or y1 >= b2)

def crop_randomly(image, crop_size):
    """
    Crops a random portion of the image with the given crop size.

    Args:
        image (np.ndarray): The image to crop.
        crop_size (int): The size of the crop.

    Returns:
        np.ndarray: The cropped image.
    """
    height, width, _ = image.shape
    x = np.random.randint(0, width - crop_size)
    y = np.random.randint(0, height - crop_size)
    return image[y:y+crop_size, x:x+crop_size]

def count_color_pixels(image, color):
    """
    Counts the number of pixels of the specified color in the image.

    Args:
        image (np.ndarray): The image in which to count the pixels.
        color (list): The RGB color to count.

    Returns:
        int: The number of pixels of the specified color.
    """
    return np.sum(np.all(image == color, axis=-1))

def calculate_statistics(pixel_counts):
    """
    Calculates statistical measures (mean, median, etc.) for a list of pixel counts.

    Args:
        pixel_counts (list): List of pixel counts.

    Returns:
        dict: Dictionary containing statistical measures.
    """
    return {
        'average': np.mean(pixel_counts),
        'std_dev': np.std(pixel_counts),
        'min': np.min(pixel_counts),
        'max': np.max(pixel_counts)
    }