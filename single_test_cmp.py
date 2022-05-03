import warnings
warnings.filterwarnings("ignore")
import keras
import tensorflow as tf
import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from keras.models import model_from_json
import pickle

fileName = askopenfilename()  
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


ou=ou.flatten()
ou=ou.reshape(1,51529)

svm_model=pickle.load(open('svm_model.pkl','rb'))
out=svm_model.predict(ou/255)

print('SVM : ',out[0])

rf_model=pickle.load(open('rf_model.pkl','rb'))
out=rf_model.predict(ou/255)
print('RF : ',out[0])

json_file = open('ann_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("ann_model.h5")



OUT=loaded_model.predict(ou/255)

X=np.argmax(OUT,axis=1)

print('ANN : ',X[0])

