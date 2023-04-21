from PIL import Image, ImageFilter  # Python Image Library
# Also, check OpenCV

img = Image.open('./photos/papaya.png')

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save('photos/papaya_filtered.png', 'png')

converted_image = img.convert('L')
converted_image.save('photos/papaya_converted.png', 'png')

rotated_image = img.rotate(90)
rotated_image.save('photos/papaya_rotated.png', 'png')

resized_image = img.resize((200,200))
resized_image.save('photos/papaya_resized.png', 'png')

box = (100,100,400,400)
converted_image = img.convert('L')
region = converted_image.crop(box)
region.save('photos/papaya_cropped.png', 'png')


processed_image = img.filter(ImageFilter.BLUR)
processed_image = processed_image.convert('L')
processed_image = processed_image.rotate(90)
processed_image = processed_image.resize((200,200))
processed_image.save('photos/papaya_processed.png', 'png')

img_2 = Image.open('./photos/beauty.jpg')
img_2.thumbnail((400,400))  # keep the aspect ratio with the tuple as max values
img_2.save('photos/beauty_thumbnail.png', 'png')

