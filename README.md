# Todo App Crud Using Flask

Information about the application

**1:** Install Python 3.10 on your Machine
**2:** Install venv using thw following command in shell
       (`pip install venv`)

**3:** clone the project from git repository

**4:** after cloning the project from repository activate virtual environment
install pipenv for creating the virtual environment
use command `pip install pipenv` after installing the pipenv
create the virtual environment with pipenv

by using the following command:
(`pipenv install`)

**5:** after installing requirements rename the .env_sample file into .env file
or run following commands
go in the server directory and run command (`flask run`)

for the Decryption of the Respone
code is givien:
(`<html lang="en">
        <body>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
            <script>
            var encrypted =
                "SWBoEbQmmNXQCntYDW0foClQC1kO2khFzyLygn63nh2jsPNJw0+Cc6RcdTFMpZgiXR4LPfPj7lpGflT5BopnWf2qn6rywWmuF1i7GHskcI4="
            var key = "AAAAAAAAAAAAAAAA"; //key used in Python
            key = CryptoJS.enc.Utf8.parse(key);
            var decrypted = CryptoJS.AES.decrypt(encrypted, key, {
                mode: CryptoJS.mode.ECB,
            });
            console.log(decrypted.toString(CryptoJS.enc.Utf8));
            </script>
        </body>
    </html>`)

decryption function is also available in app/utils.py decrypt_js(key, decrypted)
