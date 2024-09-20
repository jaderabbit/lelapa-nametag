import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Function to generate image with name
def generate_nametag(name):
    # Create an image with white background
    img = Image.new('RGB', (113, 188), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Load a font
    font = ImageFont.load_default()
    
    # Position the text in the center
    bbox = d.textbbox((0, 0), name, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    position = ((img.width - text_width) / 2, (img.height - text_height) / 2)
    
    # Add text to image
    d.text(position, name, fill=(0, 0, 0), font=font)
    
    # Save the image
    img_path = f"{name}_nametag.png"
    img.save(img_path)
    
    return img, img_path

# Streamlit app
st.title('Name Tag Generator')

# Input for name
name = st.text_input('Enter your name:')

if name:
    # Generate image
    img, img_path = generate_nametag(name)
    
    # Display image
    st.image(img, caption='Generated Name Tag')
    
    # Provide download link
    with open(img_path, "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name=img_path,
            mime="image/png"
        )