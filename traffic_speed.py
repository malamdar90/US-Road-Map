from PIL import Image
import csv

# Set Constants
center = (36.209, -118.646)
h = 0.6
w = 0.6
zoom = 8

color1 = (63, 141, 66)
color2 = (252, 169, 73)
color3 = (198, 51, 41)
background = (0, 0, 0)

# Read CSV File
csv_file_path = '/averag.csv'
with open(csv_file_path, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    lines = [line for line in spamreader]

# Set Plot Limits
ylim = (center[0] - zoom * h, center[0] + zoom * h)
xlim = (center[1] - zoom * w, center[1] + zoom * w)

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
            pix[x, y] = color1
        elif 45 < speed:
            pix[x, y] = color2
        elif 20 < speed:
            pix[x, y] = color3

# Save Image
im.save("C:/Users/malamda1/Desktop/LA.png", "PNG")
