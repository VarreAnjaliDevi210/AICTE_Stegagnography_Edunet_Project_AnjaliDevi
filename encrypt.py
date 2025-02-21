import cv2

def encrypt_image():
    img = cv2.imread("mypic.jpg")  # Replace with the correct image path

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    d = {chr(i): i for i in range(255)}
    
    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    print("Image encrypted and saved as 'encryptedImage.jpg'.")

if __name__ == "__main__":
    encrypt_image()