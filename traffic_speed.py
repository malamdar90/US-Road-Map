from PIL import Image
import csv

with open('Average_speed.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    lines = [line for line in spamreader]


h = 60000
w = 26000
xm = -126
hm = 24


im = Image.new("RGB", (h, w), (0, 0, 0))
pix = im.load()

for i in range(len(lines)):
    lat = float(lines[i][0])
    lng = float(lines[i][1])
    speed = float(lines[i][4])
    
    x = int(round(1000*(lng-xm), 0))
    y = w - int(round(1000*(lat-hm), 0))

    if 0 < x < h and 0 < y < w:
        if speed > 60:
            pix[x, y] = (63, 141, 66)
        elif 45 < speed:
            pix[x, y] = (252, 169, 73)
        elif 25 < speed:
            pix[x, y] = (198, 51, 41)


im.save("traffic_speed.png", "PNG")