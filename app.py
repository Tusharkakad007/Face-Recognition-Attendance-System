import streamlit as st
# import face_recognition
import streamlit as st

try:
    import face_recognition
    st.success("face_recognition imported successfully")
except Exception as e:
    st.exception(e)
    st.stop()
import os
import pickle
import datetime
from PIL import Image
import numpy as np


DB_DIR = "db"
LOG_FILE = "log.txt"

os.makedirs(DB_DIR, exist_ok=True)


st.set_page_config(
    page_title="Face Attendance System",
    layout="centered"
)


st.title("🔐 Face Recognition Attendance System")


mode = st.sidebar.selectbox(
    "Choose Action",
    [
        "Register User",
        "Login",
        "Logout"
    ]
)



image = st.camera_input(
    "Take a picture"
)



def save_log(name, action):

    with open(LOG_FILE,"a") as f:

        f.write(
            f"{name},{datetime.datetime.now()},{action}\n"
        )



def get_encoding(img):

    img_array = np.array(img)

    encodings = face_recognition.face_encodings(
        img_array
    )

    if len(encodings)==0:
        return None

    return encodings[0]



def recognize_face(img):

    encoding = get_encoding(img)

    if encoding is None:
        return None


    for file in os.listdir(DB_DIR):

        if file.endswith(".pickle"):

            with open(
                os.path.join(DB_DIR,file),
                "rb"
            ) as f:

                known_encoding = pickle.load(f)



            result = face_recognition.compare_faces(
                [known_encoding],
                encoding
            )


            if result[0]:

                return file.replace(
                    ".pickle",
                    ""
                )


    return None



if image:


    img = Image.open(image)


    st.image(
        img,
        caption="Captured Image"
    )



    if mode=="Register User":


        name = st.text_input(
            "Enter username"
        )


        if st.button("Register"):


            encoding = get_encoding(img)


            if encoding is None:

                st.error(
                    "No face detected"
                )


            else:

                with open(
                    f"{DB_DIR}/{name}.pickle",
                    "wb"
                ) as f:

                    pickle.dump(
                        encoding,
                        f
                    )


                st.success(
                    f"{name} registered successfully"
                )



    elif mode=="Login":


        if st.button("Login"):


            name = recognize_face(img)


            if name:

                save_log(
                    name,
                    "login"
                )


                st.success(
                    f"Welcome {name}"
                )

            else:

                st.error(
                    "Unknown person"
                )



    elif mode=="Logout":


        if st.button("Logout"):


            name = recognize_face(img)


            if name:

                save_log(
                    name,
                    "logout"
                )


                st.success(
                    f"Goodbye {name}"
                )

            else:

                st.error(
                    "Unknown person"
                )