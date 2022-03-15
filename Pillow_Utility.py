from PIL import Image, ImageDraw, Image, ImageFont

"""
To install the Pillow library
    pip install Pillow
"""

def draw_borders(pillow_image, bounding, color, image_size, caption='', confidence_score=0):

    width, height = image_size
    draw = ImageDraw.Draw(pillow_image)
    draw.polygon([
        bounding.normalized_vertices[0].x *
        width, bounding.normalized_vertices[0].y * height,
        bounding.normalized_vertices[1].x *
        width, bounding.normalized_vertices[1].y * height,
        bounding.normalized_vertices[2].x *
        width, bounding.normalized_vertices[2].y * height,
        bounding.normalized_vertices[3].x * width, bounding.normalized_vertices[3].y * height], fill=None, outline=color)

    #TODO: Validation needed
    font_size = width * height // 22000 if width * height > 400000 else 12

    font = ImageFont.truetype("arialbi.ttf", 28)
    draw.text((bounding.normalized_vertices[0].x * width,
               bounding.normalized_vertices[0].y * height), font=font, text=caption, fill=color)

    # insert confidence score
    draw.text((bounding.normalized_vertices[0].x * width, bounding.normalized_vertices[0].y *
               height + 20), font=font, text='{:.1f}'.format(float(confidence_score)), fill=color)
  
    return pillow_image