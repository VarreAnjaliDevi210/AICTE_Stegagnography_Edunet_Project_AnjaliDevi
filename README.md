# Image Steganography Tool

This project consists of two Python scripts that allow you to **encrypt** and **decrypt** secret messages within an image using steganography. The tool modifies the pixel values of the image to hide the message, which can later be extracted using the correct passcode.

## Files

1. **`encrypt.py`**: Encrypts a secret message into an image.
2. **`decrypt.py`**: Decrypts the hidden message from the encrypted image.
3. **`README.md`**: This file, providing instructions for use.

## Requirements

- Python 3.x
- OpenCV library (`cv2`)

You can install OpenCV using pip:
```bash
pip install opencv-python
```

## Usage

### Step 1: Encrypt a Message
1. Place the image you want to use (e.g., `mypic.jpg`) in the same directory as the scripts.
2. Run the `encrypt.py` script:
   ```bash
   python encrypt.py
   ```
3. Enter the **secret message** and a **passcode** when prompted.
4. The script will create a new file called `encryptedImage.jpg` with the hidden message embedded in it.

### Step 2: Decrypt the Message
1. Run the `decrypt.py` script:
   ```bash
   python decrypt.py
   ```
2. Enter the **passcode** when prompted.
3. If the passcode is correct, the script will extract and display the hidden message from the `encryptedImage.jpg` file.

## Example

1. Encrypt a message:
   ```bash
   python encrypt.py
   ```
   - Input:
     ```
     Enter secret message: Hello, World!
     Enter a passcode: mypassword
     ```
   - Output: `encryptedImage.jpg` is created.

2. Decrypt the message:
   ```bash
   python decrypt.py
   ```
   - Input:
     ```
     Enter passcode for Decryption: mypassword
     Confirm passcode: mypassword
     ```
   - Output:
     ```
     Decrypted message: Hello, World!
     ```

## Notes
- Ensure the original image (`mypic.jpg`) is in the same directory as the scripts.
- The passcode is case-sensitive and must match during encryption and decryption.
- The decryption process assumes the message length is known or can be derived. Adjust the range in `decrypt.py` if necessary.
