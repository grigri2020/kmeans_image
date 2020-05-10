import sys,os
import cv2 as cv
from PIL import Image 
import numpy as np
import matplotlib as mt
from matplotlib import image as mt_im
from matplotlib import pyplot as plt

#Read the image using cv2
def read_image(file):
    image = mt_im.imread(file)    
    return (image)

#reshape the numpy array
def reshape_image(image, size):
    return (image.reshape(-1,size))

#Read the output k-means clustered file and show it
def show_image(file):
    im = Image.open(file)
    im.show()
    
def main():
    image    = read_image("/data/cancer.jpg")
    re_image = reshape_image(image, shape[2])
    plt.hist(re_image)
    plt.show()
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    #plt.hist(re_image),plt.show()
    # Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
    #criteria is a 3 parameter tuple 
    #print (criteria)
    
    # Set flags for centers of the clusters.
    flags = cv.KMEANS_RANDOM_CENTERS
    k=10
    re_image = np.float32(re_image)
    # Apply KMeans
    compactness,labels,centers = cv.kmeans(re_image,k,None,criteria,10,flags)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    res2 = res.reshape(image.shape)
    
    #writes a file which  has the number of k in the suffix.
    #in this example it will be segmented_10.jpg
    file_out = 'segmented_' + str(k) + '.jpg' 
    cv.imwrite(file_out, res2)
    
    #compactness descreases as we go up in k (more clusters has less compactness)
    print(compactness)
    #Use PIL to read file and show the image that  was generated after clustering
    show_image(file_out)
    



    
if __name__ == "__main__":
    main()
    
    


