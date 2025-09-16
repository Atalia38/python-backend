import pandas as pd

# Read data from a CSV file
df = pd.read_csv("data.csv")

# Show first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Count missing values
print("\nMissing values in each column:")
print(df.isnull().sum())


from PIL import Image, ImageFilter

# Open an image
img = Image.open("sample.jpg")

# Resize the image
resized_img = img.resize((200, 200))
resized_img.save("resized.jpg")

# Crop part of the image (x1, y1, x2, y2)
cropped_img = img.crop((50, 50, 250, 250))
cropped_img.save("cropped.jpg")

# Apply a blur filter
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.save("blurred.jpg")







