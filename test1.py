import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import *
from qrcode.image.styles.colormasks import *

import PIL
from PIL import Image, ImageDraw


#---------------important----------------
def style_inner_eyes(img,form = "square"):
  img_size = img.size[0]
  eye_size = 120 #default 70
  quiet_zone = 40 #default
  mask = Image.new('L', img.size, 0)
  draw = ImageDraw.Draw(mask)
  if form == "square":
    draw.rectangle((60, 60, 160, 160), fill=255) #top left eye
    draw.rectangle((img_size-160, 60, img_size-60, 160), fill=255) #top right eye
    draw.rectangle((60, img_size-160, 160, img_size-60), fill=255) #bottom left eye
  if form == "rounded":
    draw.rounded_rectangle((60, 60, 160, 160), fill=255, radius=20) #top left eye
    draw.rounded_rectangle((img_size-160, 60, img_size-60, 160), fill=255, radius=20) #top right eye
    draw.rounded_rectangle((60, img_size-160, 160, img_size-60), fill=255, radius=20) #bottom left eye
  if form == "circle":
    draw.ellipse((60, 60, 90, 90), fill=255) #top left eye
    draw.ellipse((img_size-90, 60, img_size-60, 90), fill=255) #top right eye
    draw.ellipse((60, img_size-90, 90, img_size-60), fill=255) #bottom left eye
  return mask

def style_outer_eyes(img, form="square"):
  img_size = img.size[0]
  eye_size = 120 #default 70
  quiet_zone = 40 #default
  mask = Image.new('L', img.size, 0)
  draw = ImageDraw.Draw(mask)
  if form == "square":
    # draw.rectangle((40, 40, 200, 200), fill=255) #top left eye
    # draw.rectangle((img_size-200, 40, img_size-40, 200), fill=255) #top right eye
    # draw.rectangle((40, img_size-200, 200, img_size-40), fill=255) #bottom left eye
    # draw.rectangle((60, 60, 160, 160), fill=0) #top left eye
    # draw.rectangle((img_size-160, 60, img_size-60, 160), fill=0) #top right eye
    # draw.rectangle((60, img_size-160, 160, img_size-60), fill=0) #bottom left eye  
    draw.rectangle((40, 40, 110, 110), fill=255) #top left eye
    draw.rectangle((img_size-110, 40, img_size-40, 110), fill=255) #top right eye
    draw.rectangle((40, img_size-110, 110, img_size-40), fill=255) #bottom left eye
    draw.rectangle((60, 60, 90, 90), fill=0) #top left eye
    draw.rectangle((img_size-90, 60, img_size-60, 90), fill=0) #top right eye
    draw.rectangle((60, img_size-90, 90, img_size-60), fill=0) #bottom left eye  
  if form == "rounded":
    draw.rounded_rectangle((40, 40, 200, 200), fill=255, radius=20) #top left eye
    draw.rounded_rectangle((img_size-200, 40, img_size-40, 200), fill=255, radius=20) #top right eye
    draw.rounded_rectangle((40, img_size-200, 200, img_size-40), fill=255, radius=20) #bottom left eye
    draw.rounded_rectangle((60, 60, 160, 160), fill=0, radius=20) #top left eye
    draw.rounded_rectangle((img_size-160, 60, img_size-60, 160), fill=0, radius=20) #top right eye
    draw.rounded_rectangle((60, img_size-160, 160, img_size-60), fill=0, radius=20) #bottom left eye  
  if form == "circle":
    draw.ellipse((40, 40, 110, 110), fill=255) #top left eye
    draw.ellipse((img_size-110, 40, img_size-40, 110), fill=255) #top right eye
    draw.ellipse((40, img_size-110, 110, img_size-40), fill=255) #bottom left eye
    draw.ellipse((60, 60, 90, 90), fill=0) #top left eye
    draw.ellipse((img_size-90, 60, img_size-60, 90), fill=0) #top right eye
    draw.ellipse((60, img_size-90, 90, img_size-60), fill=0) #bottom left eye  

  return mask
#---------------important----------------

# cool_img = Image.open("231.jpg")
# size = (300,300)
# cool_img = cool_img.resize(size)
# cool_img.save("test.jpg")

if not hasattr(PIL.Image, 'Resampling'):
  PIL.Image.Resampling = PIL.Image

def make_qr(qr_data, 
            bor_len=2, 
            vers= 1, 
            image_center = None, 
            black_form = SquareModuleDrawer(), 
            gradient = SolidFillColorMask((255, 255, 255),(0,0,0)), 
            inner_eye_form = SquareModuleDrawer(), 
            outer_eye_form= SquareModuleDrawer(), 
            inner_gradient = SolidFillColorMask((255, 255, 255),(0,0,0)), 
            outer_gradient = SolidFillColorMask((255, 255, 255),(0,0,0)),
            eye_add = 0):
  qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, version=vers, box_size=20, border= bor_len)
  qr.add_data(qr_data)

  if image_center == None:
      img = qr.make_image(image_factory=StyledPilImage, module_drawer=black_form, color_mask=gradient)  
  else:
      img = qr.make_image(image_factory=StyledPilImage, module_drawer=black_form, color_mask=gradient, embeded_image_path=image_center)  

  if eye_add == 1:
    img_width = img.size[0]
    img_height = img.size[1]
    white_image = Image.new("RGB", (img_width, img_height), "black")
    # inner_eye_img = qr.make_image(image_factory=StyledPilImage, module_drawer=black_form, color_mask=inner_gradient, eye_drawer=inner_eye_form)
    # outer_eye_img = qr.make_image(image_factory=StyledPilImage, module_drawer=black_form, color_mask=outer_gradient, eye_drawer=outer_eye_form)    
    inner_eye_mask = style_inner_eyes(img,"circle")
    outer_eye_mask = style_outer_eyes(img,"circle")
    intermediate_img = Image.composite(white_image, img, inner_eye_mask)
    final_image = Image.composite(white_image, intermediate_img, outer_eye_mask)
    return final_image
  else:
    return img

# Now PIL.Image.Resampling.BICUBIC is always recognized.


# qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# qr.add_data('http://www.medium.com')

# qr_inner_eyes_img = qr.make_image(image_factory=StyledPilImage,
#                             eye_drawer=RoundedModuleDrawer(radius_ratio=1.2),
#                             color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(63, 42, 86)))

# qr_outer_eyes_img = qr.make_image(image_factory=StyledPilImage,
#                             eye_drawer=VerticalBarsDrawer(),
#                             color_mask=SolidFillColorMask(front_color=(255, 128, 0)))                            

# qr_img = qr.make_image(image_factory=StyledPilImage,
#                        module_drawer=SquareModuleDrawer())

# inner_eye_mask = style_inner_eyes(qr_img)
# outer_eye_mask = style_outer_eyes(qr_img)
# intermediate_img = Image.composite(qr_inner_eyes_img, qr_img, inner_eye_mask)
# final_image = Image.composite(qr_outer_eyes_img, intermediate_img, outer_eye_mask)
# final_image.save('final_image.png')

qr_img = make_qr(qr_data="Utochka: krya krya", 
                 black_form = RoundedModuleDrawer(), #форма кубиков
                 gradient = VerticalGradiantColorMask((255,255,255), (30,30,30), (90,90,30)),
                 eye_add = 1
                )

qr_img.save('userqr9090.png')