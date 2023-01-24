import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

## AES Encryption used for encrypting endpoint data
def encrypt(key, data):
    _data = str(data)
    encoded_data = pad(_data.encode(), AES.block_size)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(encoded_data)).decode('utf-8')

## AES Decryption used for decrypting endpoint data
def decrypt(key, data):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(data)), AES.block_size).decode('utf-8')

def decrypt_js(key,data):
    # <html lang="en">
    #     <body>
    #         <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    #         <script>
    #         var encrypted =
    #             "SWBoEbQmmNXQCntYDW0foClQC1kO2khFzyLygn63nh2jsPNJw0+Cc6RcdTFMpZgiXR4LPfPj7lpGflT5BopnWf2qn6rywWmuF1i7GHskcI4="
    #         var key = "AAAAAAAAAAAAAAAA"; //key used in Python
    #         key = CryptoJS.enc.Utf8.parse(key);
    #         var decrypted = CryptoJS.AES.decrypt(encrypted, key, {
    #             mode: CryptoJS.mode.ECB,
    #         });
    #         console.log(decrypted.toString(CryptoJS.enc.Utf8));
    #         </script>
    #     </body>
    # </html>`)
    pass
