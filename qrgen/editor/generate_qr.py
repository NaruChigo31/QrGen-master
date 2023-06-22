import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import *
from qrcode.image.styles.colormasks import *

import PIL
from PIL import Image, ImageDraw


def style_inner_eyes(img, form="square", inner_color = (0,0,0), bg_col = (255,255,255)):
  img_size = img.size[0]
  eye_size = 120 #default 
  quiet_zone = 40 #default
  draw = ImageDraw.Draw(img)
  if form == "square":
    draw.rectangle((75, 75, 145, 145), fill=inner_color) #top left eye
    draw.rectangle((img_size-145, 75, img_size-75, 145), fill=inner_color) #top right eye
    draw.rectangle((75, img_size-145, 145, img_size-75), fill=inner_color) #bottom left eye
  if form == "rounded":
    draw.rounded_rectangle((75, 75, 145, 145), fill=inner_color, radius=15) #top left eye
    draw.rounded_rectangle((img_size-145, 75, img_size-75, 145), fill=inner_color, radius=15) #top right eye
    draw.rounded_rectangle((75, img_size-145, 145, img_size-75), fill=inner_color, radius=15) #bottom left eye
  if form == "circle":
    draw.ellipse((75, 75, 145, 145), fill=inner_color) #top left eye
    draw.ellipse((img_size-145, 75, img_size-75, 145), fill=inner_color) #top right eye
    draw.ellipse((75, img_size-145, 145, img_size-75), fill=inner_color) #bottom left eye
  return img

def style_outer_eyes(img, form="square", outer_col = (0,0,0), bg_col = (255,255,255)):
  img_size = img.size[0]
  eye_size = 140 #default 
  quiet_zone = 40 #default
  draw = ImageDraw.Draw(img)
  if form == "square":
    draw.rectangle((40, 40, 180, 180), fill=outer_col) #top left eye
    draw.rectangle((img_size-180, 40, img_size-40, 180), fill=outer_col) #top right eye
    draw.rectangle((40, img_size-180, 180, img_size-40), fill=outer_col) #bottom left eye
    draw.rectangle((60, 60, 160, 160), fill=bg_col) #top left eye
    draw.rectangle((img_size-160, 60, img_size-60, 160), fill=bg_col) #top right eye
    draw.rectangle((60, img_size-160, 160, img_size-60), fill=bg_col) #bottom left eye  
  if form == "rounded":
    draw.rounded_rectangle((40, 40, 180, 180), fill=outer_col, radius=40) #top left eye
    draw.rounded_rectangle((img_size-180, 40, img_size-40, 180), fill=outer_col, radius=40) #top right eye
    draw.rounded_rectangle((40, img_size-180, 180, img_size-40), fill=outer_col, radius=40) #bottom left eye
    draw.rounded_rectangle((60, 60, 160, 160), fill=bg_col, radius=40) #top left eye
    draw.rounded_rectangle((img_size-160, 60, img_size-60, 160), fill=bg_col, radius=40) #top right eye
    draw.rounded_rectangle((60, img_size-160, 160, img_size-60), fill=bg_col, radius=40) #bottom left eye  
  if form == "circle":
    draw.ellipse((40, 40, 180, 180), fill=outer_col) #top left eye
    draw.ellipse((img_size-180, 40, img_size-40, 180), fill=outer_col) #top right eye
    draw.ellipse((40, img_size-180, 180, img_size-40), fill=outer_col) #bottom left eye
    draw.ellipse((60, 60, 160, 160),  fill= bg_col) #top left eye
    draw.ellipse((img_size-160, 60, img_size-60, 160),  fill= bg_col) #top right eye
    draw.ellipse((60, img_size-160, 160, img_size-60),  fill= bg_col) #bottom left eye

  return img

def no_eyes_rect(img, bg_col = (255,255,255)):
  img_size = img.size[0]
  eye_size = 140 #default 
  quiet_zone = 40 #default
  draw = ImageDraw.Draw(img)
  draw.rectangle((0, 0, 180, 180), fill=bg_col) #top left eye
  draw.rectangle((img_size-180, 0, img_size, 180), fill=bg_col) #top right eye
  draw.rectangle((0, img_size-180, 180, img_size), fill=bg_col) #bottom left eye
  draw.rectangle((0, 0, img_size, 39), bg_col)
  draw.rectangle((0, 0, 39, img_size), bg_col)
  draw.rectangle((img_size-39, 0, img_size, img_size), bg_col)
  draw.rectangle((0, img_size-39, 180, img_size), bg_col) 
  draw.line((40, img_size-181, 180, img_size-181), fill=bg_col, width=2)
  draw.line((img_size-181, 40, img_size-181, 180), fill=bg_col, width=2)
  return img

if not hasattr(PIL.Image, 'Resampling'):
  PIL.Image.Resampling = PIL.Image

def make_qr(qr_data, 
            bor_len=2, 
            vers= 1, 
            image_center = None, 
            black_form = SquareModuleDrawer(), 
            gradient = SolidFillColorMask((0,0,0),(255, 255, 255)), 
            bg_color = (255,255,255),
            inner_color = (0,0,0), 
            outer_color = (0,0,0),
            real_inner_eye_form = "square",
            real_outer_eye_form = "square",
            eye_add = 0):
  qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, version=vers, box_size=20, border= bor_len)
  qr.add_data(qr_data)

  if eye_add == 1:
    if image_center == None:
      img = qr.make_image(image_factory=StyledPilImage, module_drawer=black_form, color_mask=gradient)  
    else:
      img = qr.make_image(image_factory=StyledPilImage, module_drawer=black_form, color_mask=gradient, embeded_image_path=image_center) 
    
    no_eye_img = no_eyes_rect(img, bg_color) 
    outer_img = style_outer_eyes(no_eye_img, real_outer_eye_form, outer_color, bg_color)
    inner_img = style_inner_eyes(outer_img, real_inner_eye_form, inner_color, bg_color)
    final_image = inner_img
    return final_image
  else:
    if image_center == None:
      img = qr.make_image(image_factory=StyledPilImage, module_drawer=black_form, color_mask=gradient)  
    else:
      img = qr.make_image(image_factory=StyledPilImage, module_drawer=black_form, color_mask=gradient, embeded_image_path=image_center)  
    return img

# qr_img = make_qr(qr_data="Utochka: krya krya", 
#                  black_form = RoundedModuleDrawer(), #форма кубиков
#                  gradient = SolidFillColorMask((255,255,255),(0,0,0)),
#                  real_inner_eye_form = "circle",
#                  real_outer_eye_form = "rounded",
#                  bg_color = (255,255,255),
#                  inner_color = (0,0,0), 
#                  outer_color = (0,0,0),
#                  eye_add = 1
#                 )

# qr_img.save('userqr9092.png')