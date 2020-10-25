from skimage import metrics
import numpy as np
import cv2
import pandas as pd
import time
import os
import logging

def read_csv(input_file_path):
    """
    :param input_file_path str: The full path to the image
    :returns the pandas read CSV
    Reading the file with full path obtained from the customer input
    """
    csvfile = pd.read_csv(input_file_path)
    return csvfile

def mean_squared_error(imageA, imageB):
    """
    :param imageA obj: A CV2 Image object to compare
    :param imageB obj: A secondary CV2 Image object to compare
    :returns an error index, the lower the error the more similar they are
    The 'Mean Squared Error' between the two images is the
    sum of the squared difference between the two images;
    NOTE: the two images must have the same dimension
    """
    logging.debug("mean_squared_error")
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the mean_squared_error, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB):
    """
    Compute the mean squared error and structural similarity
    :param imageA obj: A CV2 Image object to compare
    :param imageB obj: A secondary CV2 Image object to compare
    :returns tuple composed of mean_squared_error and negated structural_similarity
    """
    logging.debug("compare_images")
    mse = mean_squared_error(imageA, imageB)
    similarity = metrics.structural_similarity(imageA, imageB)
    return mse, 1-similarity


def compare(filePath1, filePath2):
    """
    Opens, imports and compares two file paths that should be images
    :param filePath1: The full path to an image file.
    :param filePath2: The full path to a secondary image file.
    :returns tuple with mean_squared_error, structural_similarity
              and the duration of the processing
    """
    start = time.time()
    image1 = cv2.imread(filePath1)
    image2 = cv2.imread(filePath2)
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    dim = (1024, 768)
    image1 = cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)
    image2 = cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)
    end = time.time()
    duration = end - start
    m, s = compare_images(image1, image2)
    return m, s, duration


def process_csv(input_file_path, output_file_path="Result.csv"):
    """
    Loads the CSV and iterates over the rows to provide similary and processing cost
    :param input_file_path str: The two-column file name containing image paths
    :param output_file_path str: The location to store the process of the input rows
    """
    logging.debug("process_csv")
    csvfile = read_csv(input_file_path)
    print(csvfile.head(5))

    # for loop inside an iteration to evaluate the previous results:
    # empty arrays
    similar = []
    elapsed = []
    for _index, row in csvfile.iterrows():
        filePath1 = row['Image1']
        filePath2 = row['Image2']
        logging.debug("Processing files '{}' and '{}':".format(row['Image1'], row['Image2']))
        m, s, d = compare(filePath1, filePath2)
        similar.append(s)
        elapsed.append(d)
        print(m, s, d)
        if (1-s > 0.9):
            logging.debug("Match")
        else:
            logging.debug("Different")

    csvfile["similar"] = similar
    csvfile["elapsed"] = elapsed
    csvfile.to_csv(output_file_path)
