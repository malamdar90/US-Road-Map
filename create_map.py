from PIL import Image
import csv

# Constants
c = (36.0, -118.5)
margin = (5, 5)

# Colors
c_high = (60, 140, 60)
c_med = (250, 170, 70)
c_low = (200, 50, 40)
bg = (0, 0, 0)

# Speed Lower Bounds in mph
high_lb, med_lb, low_lb = 60, 45, 20

# Read CSV File
csv_path = '/averag_speed.csv'
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [line for line in csv_reader]

# Lat/long Intervals
lat_int = (c[0] - margin[0], c[0] + margin[0])
lng_int = (c[1] - margin[1], c[1] + margin[1])

# Calculate Plot Dimensions
h = int(round(1000 * (lat_int[1] - lat_int[0]), 0) + 1)
w = int(round(1000 * (lng_int[1] - lng_int[0]), 0) + 1)

# Create Image
img = Image.new("RGB", (w, h), bg)
pix = img.load()

# Plot Points on Image
for i in range(len(data)):
    lat = float(data[i][0])
    lng = float(data[i][1])
    spd = float(data[i][3])

    if lng_int[0] < lng < lng_int[1] and lat_int[0] < lat < lat_int[1]:
        x = int(round(1000 * (lng - lng_int[0]), 0))
        y = int(round(1000 * (lat_int[1] - lat), 0))

        if spd > high_lb:
            pix[x, y] = c_high
        elif spd > med_lb:
            pix[x, y] = c_med
        elif spd > low_lb:
            pix[x, y] = c_low

# Save Image
img.save("/socal.png", "PNG")
