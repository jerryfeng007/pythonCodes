from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rnd():
    return chr(random.randint(65, 90))


def color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def color2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


width = 300
height = 120
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 100)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=color())

for t in range(4):
    draw.text((60 * t + 10, 10), rnd(), font=font, fill=color2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
