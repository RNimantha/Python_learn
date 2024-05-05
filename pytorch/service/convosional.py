
import os
import cv2
import numpy as np
from tqdm import tqdm
REBUILD_DATA = True

class Convo():
    def __init__(self):
        self.IMG_SIZE = 50
        self.CATS = "PetImages/Cat"
        self.DOGS = "PetImages/Dog"
        self.TESTING = "PetImages/Testing"
        self.LABELS = {self.CATS: 0, self.DOGS: 1}
        self.training_data = []

    def convo(self):
        for label in self.LABELS:
            print(label)
            for f in tqdm(os.listdir(label)):
                if "jpg" in f:
                    try:
                        path = os.path.join(label, f)
                        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                        img = cv2.resize(img, (self.IMG_SIZE, self.IMG_SIZE))
                        self.training_data.append([np.array(img), np.eye(2)[self.LABELS[label]]])  # do something like print(np.eye(2)[1]), just makes one_hot 
                        #print(np.eye(2)[self.LABELS[label]])

                        if label == self.CATS:
                            self.catcount += 1
                        elif label == self.DOGS:
                            self.dogcount += 1

                    except Exception as e:
                        pass
                        #print(label, f, str(e))
        np.random.shuffle(self.training_data)
        np.save("training_data.npy", self.training_data)
        print(self.catcount)
        print(self.dogcount)