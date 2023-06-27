from PIL import Image
import requests
from io import BytesIO
from tkinter import Tk, Label
from PIL import ImageTk, Image

# URL of the Firebase Storage image
firebase_image_url = 'https://firebasestorage.googleapis.com/v0/b/gateactivities.appspot.com/o/icon.png?alt=media&token=7200bf70-d669-4efd-a869-cd6b5f156cd3'

# Retrieve the image from the URL
response = requests.get(firebase_image_url)
image_data = response.content

# Load the image data using Pillow
image = Image.open(BytesIO(image_data))

root = Tk()

# Convert the image data to a Tkinter-compatible format
image = Image.open(BytesIO(image_data))
photo = ImageTk.PhotoImage(image)

# Create a label widget and display the image
label = Label(root, image=photo)
label.pack()

# Run the Tkinter event loop
root.mainloop()

