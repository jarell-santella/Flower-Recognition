# Flower Recognition Project

## Progress:

### Data pipeline
#### Extract
- [x] Access all JPEG files in a directory containing multiple datasets
- [x] Determine the label of each image by looking at its path for a folder name matching an object we want to classify. Images that do not meet the criteria of having a folder name in its path that matches an object we want to classify are disregarded
#### Transform
- [x] Find longer side of each image and crop to same pixel length as shorter side, then change resolution
- [x] Convert each image to NumPy arrays of pixel data, each image being a pixel width x pixel height x RGB channels NumPy array
- [x] Create hashes for each image based on their pixel data to later identify similar images to remove and further clean the dataset
- [x] Add each image as a single row in a pandas DataFrame with 3 columns for the image's pixel data in a NumPy array, the image's hashed pixel data, and the image's label
- [x] Remove duplicate hashes from the pandas DataFrame, keeping the image with the first occurence of the hash such that all images are unique
- [x] Export this pandas DataFrame without the column for the image's hashed pixel data as a pickle, ready to load and be read
#### Load
- [ ] TBD

## Datasets
1. https://www.kaggle.com/datasets/alxmamaev/flowers-recognition
2. https://www.kaggle.com/datasets/sauravagarwal/flower-classification
3. https://www.kaggle.com/datasets/l3llff/flowers

These were not uploaded to GitHub.