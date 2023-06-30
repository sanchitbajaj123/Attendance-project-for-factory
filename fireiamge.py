from PIL import Image
import requests
from io import BytesIO
from tkinter import Tk, Label
from PIL import ImageTk, Image

# URL of the Firebase Storage image
firebase_image_url = 'https://firebasestorage.googleapis.com/v0/b/gateactivities.appspot.com/o/1688035075196?alt=media&token=1ec0434c-c362-489c-8a54-92d0a2cfd40d'

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

