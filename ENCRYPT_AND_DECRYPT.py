from PIL import Image

# Function to encrypt an image by swapping pixel values
def encrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path).convert("RGB")  # Ensure the image is in RGB mode
        pixels = img.load()

        # Encrypt the image by modifying pixel values
        for i in range(img.size[0]):  # Loop over width
            for j in range(img.size[1]):  # Loop over height
                r, g, b = pixels[i, j]

                # Apply a basic mathematical operation: Add the key to each pixel value
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

                # Set the new pixel values
                pixels[i, j] = (r, g, b)

        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")

    except Exception as e:
        print(f"An error occurred during encryption: {e}")


# Function to decrypt an image by reversing the encryption operation
def decrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path).convert("RGB")  # Ensure the image is in RGB mode
        pixels = img.load()

        # Decrypt the image by reversing the mathematical operation
        for i in range(img.size[0]):  # Loop over width
            for j in range(img.size[1]):  # Loop over height
                r, g, b = pixels[i, j]

                # Reverse the operation by subtracting the key
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

                # Set the new pixel values
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
