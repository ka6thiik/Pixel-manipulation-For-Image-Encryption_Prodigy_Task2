import os
from PIL import Image

# Function to validate output path
def validate_output_path(output_path):
    if not os.path.splitext(output_path)[1]:  # Check if no extension is provided
        raise ValueError("The output path must include a file name and extension (e.g., .png, .jpg).")

# Function to encrypt an image by modifying pixel values
def encrypt_image(image_path, output_path, key):
    try:
        validate_output_path(output_path)  # Ensure valid output path
        img = Image.open(image_path).convert("RGB")  # Ensure RGB mode
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[i, j] = (r, g, b)

        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

# Function to decrypt an image by reversing the encryption operation
def decrypt_image(image_path, output_path, key):
    try:
        validate_output_path(output_path)  # Ensure valid output path
        img = Image.open(image_path).convert("RGB")  # Ensure RGB mode
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                r = (r - key) % 256  # Reverse the shift for decryption
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[i, j] = (r, g, b)

        img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

# Main function to encrypt or decrypt an image based on user choice
def image_cipher():
    action = input("Would you like to (E)ncrypt or (D)ecrypt an image? ").upper()
    image_path = input("Enter the path to the image file: ").strip()
    output_path = input("Enter the path to save the new image: ").strip()

    try:
        key = int(input("Enter an integer key for encryption/decryption: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer key.")
        return

    if action == 'E':
        encrypt_image(image_path, output_path, key)
    elif action == 'D':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice! Please select 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    image_cipher()
