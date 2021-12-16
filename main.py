from PIL import Image, ImageDraw, ImageFont


image = Image.open('img.jpg')

font = ImageFont.load_default()


myFont = ImageFont.truetype('fonts/Ubuntu.ttf', size=150)


d1 = ImageDraw.Draw(image)


d1.text((400, 100), "Success", fill=(5, 0, 50), font=myFont)


messege = " is a journey not a Destination."


d1.text((450, 200), messege, fill=(5, 0, 50), font=myFont)


image.show()

