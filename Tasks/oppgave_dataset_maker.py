import numpy as np
import matplotlib.pyplot as plt
import os
import cv2 
import random
import pickle

training_data = []


def create_training_data(DATADIR, IMG_SIZE, CATEGORIES):

    for category in CATEGORIES:

        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        print(path)
        for img in os.listdir(path):

            try: 
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])

            except Exception as e:
                print(img)
                print("pass")
                pass
    X = []
    y = []

    for features, label in training_data:
        X.append(features)
        y.append(label)
    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    
    random.shuffle(training_data)
    
    pickle_out = open("X.pickle","wb")
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open("y.pickle","wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()

create_training_data("E:/kaggle/PetImages/", 50, (["Dog", "Cat"]))

print("Length of training data:", len(training_data))

# viser første del av datasett
#print((pickle.load(open("X.pickle", "rb")))[1])