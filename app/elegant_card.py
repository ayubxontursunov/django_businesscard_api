import os

from PIL import Image, ImageFont, ImageDraw
from django.http import Http404

from card import settings


def create_businesscard(user_data):
    jobtitle = user_data['job_title']
    phone = user_data['phone']
    email = user_data['email']
    firstname = user_data['fname']
    surname = user_data['sname']
    github = user_data['github']

    name = 'elegant_card.png'
    image_path = os.path.join(settings.MEDIA_ROOT, name)
    firstname = firstname.upper()
    surname = surname.upper()
    jobtitle = jobtitle.upper()
    if not os.path.exists(image_path):
        raise Http404("Image does not exist")

    img1 = Image.open(image_path)
    draw = ImageDraw.Draw(img1)
    W, H = img1.size

    font_name_normal = "OpenSans-Medium.ttf"
    font_path_normal = os.path.join(settings.BASE_DIR, 'app/fonts', font_name_normal)


    font_name = "OpenSans-Bold.ttf"
    font_path = os.path.join(settings.BASE_DIR, 'app/fonts', font_name)
    font_title = ImageFont.truetype(font_path, 60)
    font_normal = ImageFont.truetype(font_path_normal, 41)
    font_normal_body = ImageFont.truetype(font_path_normal, 25)
    _, _, w, h = draw.textbbox((0, 0), firstname, font=font_title)
    _, _, ws, hs = draw.textbbox((0, 0), surname, font=font_title)
    _, _, wj, hj = draw.textbbox((0, 0), jobtitle, font=font_normal)
    _, _, we, he = draw.textbbox((0, 0), email, font=font_normal_body)
    _, _, wg, hg = draw.textbbox((0, 0), github, font=font_normal_body)
    _, _, wp, hp = draw.textbbox((0, 0), phone, font=font_normal_body)

    # set firstname, and surname
    (draw.text(
        (40, 55),
        firstname, fill='#DFAF46',
        font=font_title,
    ),
     draw.text(
         (w + 60, 55),
         surname, fill='#DFAF46',
         font=font_title,
     ),)

    # set job title
    draw.text(
        (41, h + 56),
        jobtitle, fill='#DFAF46'    ,
        font=font_normal,
    )
    # set phone number
    draw.text(
        (115, h + 310),
        phone, fill='#DFAF46',
        font=font_normal_body,
    )
    # set email
    draw.text(
        (115, h + 352),
        email, fill='#DFAF46',
        font=font_normal_body,
    )
    # set email
    draw.text(
        (115, h + 397),
        github, fill='#DFAF46',
        font=font_normal_body,
    )
    image_result = os.path.join(settings.MEDIA_ROOT, f'{firstname}.png')
    img1.save(image_result)
    print('Successfully is cut and saved')
