import pickle
from pathlib import Path

import streamlit_authenticator as stauth
# Este archivo crea los usuarios y contraseñas del programa y los guarda en un archivo pkl con formato hashed
names = ["Secretaria", "Director_Pos", "Director_Prog"]
usernames = ["Secretaria", "Director_Pos", "Director_Prog"]
passwords = ["pas123", "pass344", "pass890"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
