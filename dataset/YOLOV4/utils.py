import os

directory = "rainy/"

# Change file name of images
for filename in os.listdir(directory):
    temp = filename.split('.')[0]
    os.rename(directory+filename, directory + temp + '_rain.txt')


