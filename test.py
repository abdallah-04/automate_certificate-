from PIL import Image, ImageFont, ImageDraw
import os

img_path = "D:\\my_2projects\\automate_certificate-\\Attendance badge.png"
img = Image.open(img_path)

draw = ImageDraw.Draw(img)

Fill = "white"
center_y = 400
font_path = "D:\\my_2projects\\automate_certificate-\\IMFellEnglish-Regular.ttf"
font = ImageFont.truetype(font_path, 100)

img_width, img_height = img.size
text = "Abdallah Almufleh"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (img_width - text_width) // 2
y = center_y

draw.text((x, y), text, font=font, fill=Fill)

output_path = os.path.join("C:\\Users\\Abdallah\\Desktop\\WORKSHOPS", "abdallah_certificate.pdf")
img.convert("RGB").save(output_path)
print(f"Saved: {output_path}\nText X Position: {x}")
