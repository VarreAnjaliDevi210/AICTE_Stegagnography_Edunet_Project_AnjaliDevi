import cv2

def decrypt_image():
    img = cv2.imread("encryptedImage.jpg")  # Load the encrypted image

    password = input("Enter passcode for Decryption: ")
    pas = input("Confirm passcode: ")

    if password == pas:
        c = {i: chr(i) for i in range(255)}
        
        message = ""
        n = 0
        m = 0
        z = 0

        # Assuming the length of the message is known or can be derived
        # For simplicity, we'll use a fixed length (you can modify this as needed)
        for i in range(100):  # Adjust the range based on the expected message length
            try:
                message += c[img[n, m, z]]
                n = n + 1
                m = m + 1
                z = (z + 1) % 3
            except:
                break

        print("Decrypted message:", message)
    else:
        print("YOU ARE NOT auth")

if __name__ == "__main__":
    decrypt_image()