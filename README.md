# kmeans_image
Use k-means to cluster an image. This is mostly to compress the image. Using data of a biopsy image from random google search. The example file is "cancer.jpg". Png does not work in this case so please convert your png to jpeg. 

Method:
=======
Using matplotlib, image is read into pixels. 

Parameters to use for k-means:
===============================
1. nclusters : Which is k in the k-means aka number of clusters 
2. criteria  : It is a tuple of 3 parameters. It's the iteration termination criteria.
3. flags.    : How to initialize centers for these clusters


Outputs:
=========
1. compactness  : sum of squared distance from each point to their corresponding centers
2. labels       : labels for k-means (labeled as '0', '1' etc

