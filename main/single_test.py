import warnings
warnings.filterwarnings("ignore")
import keras
import tensorflow as tf
import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def get_criminal(file):
    fileName = file
    if fileName == '':
        print('No file selected')
        print('Program Completed')
        exit()
    kernel = np.ones((2,1),np.uint8)

    imag=cv2.imread(fileName,0)

    imag=cv2.resize(imag,(227,227))



    ou = cv2.adaptiveThreshold(imag,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,5)

    ou = cv2.morphologyEx(ou, cv2.MORPH_OPEN, kernel)
    ou= ou.reshape(227,227)

    ou=255-ou
    ou=np.multiply(imag,ou)






    model = keras.models.load_model('main/modelcnncvl.h5')

    OUT=model.predict(ou.reshape(-1,227,227,1)/255)

    X=np.argmax(OUT,axis=1)

    d={0:'aesculus flava',1:'ailanthus altissima',2:'chamaecyparis thyoides',3:'evodia daniellii',4:'fraxinus pennsylvanica',5:'juniperus virginiana',6:'phellodendron amurense',
    7:'pinus parviflora',8:'quercus falcata',9:'quercus macrocarpa',10:'taxodium distichum'}
    keras.backend.clear_session()
    print(X[0])
    return X[0]

