from PIL import Image
import csv

# Constants
c = (36.0, -118.5)
lat_margin = 5
lng_margin = 5

# Colors
c_high = (60, 140, 60)
c_med = (250, 170, 70)
c_low = (200, 50, 40)
bg = (0, 0, 0)

# Speed Lower Bounds in mph
high_lb = 60
med_lb = 45
low_lb = 20

# Read CSV File
csv_path = '/averag.csv'
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data_lines = [line for line in csv_reader]

# Plot Limits
lat_int = (c[0] - lat_margin, c[0] + lat_margin)
lng_int = (c[1] - lng_margin, c[1] + lng_margin)

# Calculate Plot Dimensions
h = int(round(1000 * (lat_int[1] - lat_int[0]), 0) + 1)
w = int(round(1000 * (lng_int[1] - lng_int[0]), 0) + 1)

# Create Image
img = Image.new("RGB", (w, h), bg)
pix = img.load()

# Plot Points on Image
for i in range(len(data_lines)):
    lat = float(data_lines[i][0])
    lng = float(data_lines[i][1])
    spd = float(data_lines[i][3])

    if lng_int[0] < lng < lng_int[1] and lat_int[0] < lat < lat_int[1]:
        x = int(round(1000 * (lng - lng_int[0]), 0))
        y = int(round(1000 * (lat_int[1] - lat), 0))

        if spd > high_lb:
            pix[x, y] = c_high
        elif med_lb < spd:
            pix[x, y] = c_med
        elif low_lb < spd:
            pix[x, y] = c_low

# Save Image
img.save("/socal.png", "PNG")
