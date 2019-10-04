#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os,shutil,math,scipy,cv2
import numpy as np
import matplotlib.pyplot as plt
import random as rn


# In[5]:


from sklearn.utils import shuffle
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix,roc_curve,auc


# In[3]:


from PIL import Image
from PIL import Image as pil_image
from PIL import ImageDraw


# In[4]:


from time import time
from glob import glob
from tqdm import tqdm
from skimage.io import imread
from IPython.display import SVG


# In[5]:


from scipy import misc,ndimage
from scipy.ndimage.interpolation import zoom
import imread


# In[6]:


from keras import backend as K
from keras.utils.np_utils import to_categorical
from keras import layers
from keras.preprocessing.image import save_img
from keras.utils.vis_utils import model_to_dot
from keras.applications.vgg16 import VGG16,preprocess_input
from keras.models import Sequential,Input,Model
from keras.layers import Dense,Flatten,Dropout,Concatenate,GlobalAveragePooling2D,Lambda,ZeroPadding2D
from keras.layers import SeparableConv2D,BatchNormalization,MaxPooling2D,Conv2D
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam,SGD
from keras.utils.vis_utils import plot_model
from keras.callbacks import ModelCheckpoint,EarlyStopping,TensorBoard,CSVLogger,ReduceLROnPlateau,LearningRateScheduler


# In[7]:


def show_final_history(history):
    fig, ax = plt.subplots(1, 2, figsize=(15,5))
    ax[0].set_title('loss')
    ax[0].plot(history.epoch, history.history["loss"], label="Train loss")
    ax[0].plot(history.epoch, history.history["val_loss"], label="Validation loss")
    ax[1].set_title('acc')
    ax[1].plot(history.epoch, history.history["acc"], label="Train acc")
    ax[1].plot(history.epoch, history.history["val_acc"], label="Validation acc")
    ax[0].legend()
    ax[1].legend()


# In[8]:


def label_assignment(img,label):
    return label

def training_data(label,data_dir):
    for img in tqdm(os.listdir(data_dir)):
        label = label_assignment(img,label)
        path = os.path.join(data_dir,img)
        img = cv2.imread(path,cv2.IMREAD_COLOR)
        img = cv2.resize(img,(imgsize,imgsize))
        
        X.append(np.array(img))
        Z.append(str(label))


# In[ ]:


image_path = './Downloads/images/'

beans = image_path+'BEANS'
cake = image_path+'CAKE'
candy = image_path+'CANDY'
cereal = image_path+'CEREAL'
chips = image_path+'CHIPS'
chocolate = image_path+'CHOCOLATE'
coffee = image_path+'COFFEE'
corn = image_path+'CORN'
fish = image_path+'FISH'
flour = image_path+'FLOUR'
honey = image_path+'HONEY'
jam = image_path+'JAM'
juice = image_path+'JUICE'
milk = image_path+'MILK'
nuts = image_path+'NUTS'
oil = image_path+'OIL'
pasta = image_path+'PASTA'
rice = image_path+'RICE'
soda = image_path+'SODA'
spices = image_path+'SPICES'
sugar = image_path+'SUGAR'
tea = image_path+'TEA'
tomato_sauce = image_path+'TOMATO_SAUCE'
vinegar = image_path+'VINEGAR'
water = image_path+'WATER'

X = []
Z = []
imgsize = 150


training_data('beans',beans)
training_data('cake',cake)
training_data('candy',candy)
training_data('cereal',cereal)
training_data('chips',chips)
training_data('chocolate',chocolate)
training_data('coffee',coffee)
training_data('corn',corn)
training_data('fish',fish)
training_data('flour',flour)
training_data('honey',honey)
training_data('jam',jam)
training_data('juice',juice)
training_data('milk',milk)
training_data('nuts',nuts)
training_data('oil',oil)
training_data('psata',pasta)
training_data('rice',rice)
training_data('soda',soda)
training_data('spices',spices)
training_data('sugar',sugar)
training_data('tea',tea)
training_data('tomato sauce',tomato_sauce)
training_data('vinegar',vinegar)
training_data('water',water)


# In[ ]:


label_encoder= LabelEncoder()
Y = label_encoder.fit_transform(Z)
Y = to_categorical(Y,25)
X = np.array(X)
X=X/255

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


# In[6]:


from platform import python_version
print(python_version())


# In[ ]:




