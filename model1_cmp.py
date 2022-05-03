import warnings
warnings.filterwarnings('ignore')
import os
import cv2
#from skimage.feature import hog
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score,plot_confusion_matrix,ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.layers import Dense
from keras.models import Sequential
from keras import optimizers

path1=os.getcwd()
path=os.path.join(path1,'dataset','HeadPoseImageDatabase')

data=os.listdir(path)
kernel = np.ones((2,1),np.uint8)

out=[]
##out=np.zeros((60,227,227))
label=[]

d=0
k=0
m=0

for i in data:
    path1=os.path.join(path,i)
    print(path1)
    class_data=os.listdir(path1)
    print(class_data)
    m=d
    d=d+1
    
    da=[m for x in range(len(class_data))]
    label.extend(da)
    m=m+1
    for j in class_data:
        
        
        imag=cv2.imread(os.path.join(path1,j),0)
        imag=cv2.resize(imag,(227,227))

        ou = cv2.adaptiveThreshold(imag,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,5)
        
        ou = cv2.morphologyEx(ou, cv2.MORPH_OPEN, kernel)
        ou= ou.reshape(227,227)

        ou=255-ou
        
        ou=np.multiply(imag,ou)
        

        out.append(ou.flatten())
        
        k=k+1
        

out=np.array(out)

out=out/255


xtrain, xtest, ytrain, ytest = train_test_split(out, label, test_size = 0.3, random_state=42)

svm_model = SVC(kernel='linear',probability=True)
svm_model.fit(xtrain, ytrain)

ypred = svm_model.predict(xtest)
print('Actual targets:',ytest)
print('Predicted Targets:',ypred)
print(confusion_matrix(ytest,ypred))  
print(classification_report(ytest,ypred))
print('Accuracy:',accuracy_score(ytest, ypred))
pickle.dump(svm_model, open('svm_model.pkl', 'wb'))
plot_confusion_matrix(svm_model,xtest,ytest)
plt.title('SVM')
plt.show()

rf_model = RandomForestClassifier(max_depth=2, random_state=0)
rf_model.fit(xtrain, ytrain)
predicted3=rf_model.predict(xtest)
print('Actual targets:',ytest)
print('Predicted Targets:',predicted3)
print(confusion_matrix(ytest,predicted3)) 
print(classification_report(ytest,predicted3))
print('Accuracy:',accuracy_score(ytest, predicted3))
pickle.dump(rf_model, open('rf_model.pkl', 'wb'))
plot_confusion_matrix(rf_model,xtest,ytest)
plt.title('Random Forest')
plt.show()


xtrain, xtest, ytrain, ytest = train_test_split(out, label, test_size = 0.3, random_state=42)
yt=ytest
ytrain = np_utils.to_categorical(ytrain)
ytest = np_utils.to_categorical(ytest)
def baseline_model():

    model = Sequential()
    model.add(Dense(20, input_dim=51529, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(15, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
    return model

model = baseline_model()
print(xtrain.shape)
history=model.fit(xtrain, ytrain, validation_data=(xtest, ytest), epochs=8, batch_size=8, verbose=2)

scores = model.evaluate(xtest, ytest, verbose=0)
print("ANN Accuracy:",scores[1]*100)

model_json = model.to_json()
with open("ann_model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("ann_model.h5")
plt.title('ANN Loss')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.title('ANN Accuracy')
print(history.history)
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='test')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

y_pred = model.predict(xtest)
y_list=[]
for i in y_pred:
    print(i,type(i))
    num_list=list(i)
    print(num_list)
    output=max(num_list)
    ind=num_list.index(output)
    print(ind)
    y_list.append(ind)

cm=confusion_matrix(yt,y_list)
print(cm)
print(classification_report(yt,y_list))
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'])
disp.plot()
plt.show()