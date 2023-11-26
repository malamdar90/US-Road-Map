from PIL import Image
import csv

# Set Constants
center = (36.0, -118.5)
lat_range = 5
lng_range = 5

color_high_speed = (60, 140, 60)
color_med_speed = (250, 170, 70)
color_low_speed = (200, 50, 40)
background = (0, 0, 0)

# Read CSV File
csv_file_path = '/averag.csv'
with open(csv_file_path, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    lines = [line for line in spamreader]

# Set Plot Limits
ylim = (center[0] - lat_range, center[0] + lat_range)
xlim = (center[1] - lng_range, center[1] + lng_range)

# Calculate Plot Dimensions
plot_h = int(round(1000 * (ylim[1] - ylim[0]), 0) + 1)
plot_w = int(round(1000 * (xlim[1] - xlim[0]), 0) + 1)

# Create Image
im = Image.new("RGB", (plot_w, plot_h), background)
pix = im.load()

# Plot Points on Image
for i in range(len(lines)):
    lat = float(lines[i][0])
    lng = float(lines[i][1])
    speed = float(lines[i][3])

    if xlim[0] < lng < xlim[1] and ylim[0] < lat < ylim[1]:
        x = int(round(1000 * (lng - xlim[0]), 0))
        y = int(round(1000 * (ylim[1] - lat), 0))

        if speed > 60:
            pix[x, y] = color_high_speed
        elif 45 < speed:
            pix[x, y] = color_med_speed
        elif 20 < speed:
            pix[x, y] = color_low_speed

# Save Image
im.save("C:/Users/malamda1/Desktop/socal.png", "PNG")
