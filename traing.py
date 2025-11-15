from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from PIL import Image,ImageTk

class tran:
    def __init__(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # gray scale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])  # Fix typo here
            faces.append(imageNp)
            ids.append(id)

        ids = np.array(ids)

        try:
            # For OpenCV 4.x and above
            clf = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            # For OpenCV 3.x
            clf = cv2.face.createLBPHFaceRecognizer()

        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

