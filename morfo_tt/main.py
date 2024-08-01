import numpy as np
import pandas as pd
from processing import place_square, crop_randomly, count_color_pixels, calculate_statistics

# Parameters
num_batches = 5
batch_size = 20
image_size = (256, 512, 3)
crop_size = 200
square_size = 50
white_color = [255, 255, 255]
black_color = [0, 0, 0]

# Initialize lists to store pixel counts
white_pixel_counts = [[] for _ in range(num_batches)]
black_pixel_counts = [[] for _ in range(num_batches)]

# Generate images and count pixels
for batch in range(num_batches):
    for _ in range(batch_size):
        img_arr = np.random.randint(0, 256, image_size, dtype=np.uint8)
        occupied_areas = []
        img_arr, occupied_areas = place_square(img_arr, square_size, white_color, occupied_areas)
        img_arr, occupied_areas = place_square(img_arr, square_size, black_color, occupied_areas)
        cropped_img_arr = crop_randomly(img_arr, crop_size)
        white_pixel_counts[batch].append(count_color_pixels(cropped_img_arr, white_color))
        black_pixel_counts[batch].append(count_color_pixels(cropped_img_arr, black_color))

# Calculate statistics
white_stats = [calculate_statistics(batch) for batch in white_pixel_counts]
black_stats = [calculate_statistics(batch) for batch in black_pixel_counts]

# Prepare data for DataFrame
data = []
for i in range(num_batches):
    data.append({
        'batch_id': i + 1,
        'white_avg': white_stats[i]['average'],
        'white_min': white_stats[i]['min'],
        'white_max': white_stats[i]['max'],
        'white_std': white_stats[i]['std_dev'],
        'black_avg': black_stats[i]['average'],
        'black_min': black_stats[i]['min'],
        'black_max': black_stats[i]['max'],
        'black_std': black_stats[i]['std_dev']
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Parquet file
df.to_parquet('color_statistics.parquet')

# Display DataFrame
print(df)