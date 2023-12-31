import numpy as np
import os
import tensorflow as tf

class DataGenerator(tf.keras.utils.Sequence):
    """
    Data Generator for the disentangled VAE.
    """
    def __init__(self, data, batch_size=16, img_size=64, shuffle=True):
        
        self.imgs = data
        self.batch_size = batch_size
        self.img_size = img_size
        self.shuffle = shuffle
        self.indexes = np.arange(len(self.imgs))
        if self.shuffle:
            np.random.shuffle(self.indexes)

        self.imgs = self.preprocess_images(self.imgs)
        
    def __len__(self):
        return int(np.ceil(len(self.imgs) / self.batch_size))
    
    def __getitem__(self, index):
        batch_indexes = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]
        batch = self.imgs[batch_indexes]
        return batch
    
    def preprocess_images(self, images):
        images = images.reshape((images.shape[0], self.img_size, self.img_size, 1)).astype('float32')
        images /= 255.
        return images
    
    def on_epoch_end(self):
        if self.shuffle:
            np.random.shuffle(self.indexes)

