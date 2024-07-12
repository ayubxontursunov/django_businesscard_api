from PIL import Image, ImageDraw, ImageFont

# Define the contact information
def create_businesscard(user_data):
    name = "atb"
    # title = "DATA PRODUCT DEVELOPER"
    # title = "Backend Developer"
    #
    # phone = "+998 88 007 76 06"
    # fname = "Ayyubkhon"
    # sname = "Tursunov"
    # email = "atb@example.com"


    title = user_data['job_title']
    phone = user_data['phone']
    email = user_data['email']
    fname = user_data['fname']
    sname = user_data['sname']

    # medium_url = "medium.com/atbb"
    # github_url = "github.com/ayubxontursunov"

    # Define fonts
    font_heading = ImageFont.truetype("app/fonts/Lexend-Bold.ttf", 80)
    font_sub_heading = ImageFont.truetype("app/fonts/Lexend-Medium.ttf", 18)
    font_body = ImageFont.truetype("app/fonts/Lexend-Regular.ttf", 14)
    font_body_bold = ImageFont.truetype("app/fonts/Lexend-Bold.ttf", 14)

    # Create a blank business card
    card_width = 800
    card_height = 400
    card = Image.new("RGB", (card_width, card_height), "black")

    # Create a drawing context
    draw = ImageDraw.Draw(card)

    # Add left contents
    draw.text((60, 130), name, fill="white", font=font_heading)
    draw.line((64, 224, 64, 237), fill="green", width=4)
    draw.text((72, 220), title, fill="white", font=font_sub_heading)

    # Add right contents
    contact_prepends = ["f.", "s.", "e.", "p."]
    draw.multiline_text(
        (454, 160),
        "\n".join(contact_prepends),
        fill="green",
        font=font_body_bold,
        spacing=6,
    )
    contact_texts = [fname, sname, email, phone]
    draw.multiline_text(
        (476, 160),
        "\n".join(contact_texts),
        fill="white",
        font=font_body,
        spacing=6,
    )

    # Paste QR Code
    # qr_code = Image.open("qr-code.png").resize((80, 80))
    # card.paste(qr_code, (660, 160), qr_code)

    # Save the business card
    card.save(f"media/{fname}.png")
