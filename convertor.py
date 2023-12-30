from PIL import Image

png_image = Image.open("logo.png")
png_image.save("logo.ico", format='ICO', sizes=[(24, 24)])
