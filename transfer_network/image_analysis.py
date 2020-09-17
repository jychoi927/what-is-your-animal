import numpy as np
import scipy.ndimage
import glob
import cv2 as cv
import matplotlib.pyplot as plt
import seaborn as sns
from skimage.measure import _structural_similarity

sns.set(style="darkgrid")

''' Define SSIM'''
ssim = _structural_similarity.compare_ssim

''' Path for humans'''
path = '/home/mlpa/PycharmProjects/KJW/capstone_project/' \
       'human2animal/transfer_network/image_transfer/test_human_crop/*.*'
path = sorted(glob.glob(path))
print(path)
'''
Two options,  1. test_human, 2. test_human_crop
'''

''' Path for animals'''
path2 = '/home/cheeze/PycharmProjects/KJW/capstone_project/' \
       'human2animal/transfer_network/image_transfer/test_transfer/'
category = ['cat/*.*', 'dog/*.*', 'pig/*.*']
cat_path = sorted(glob.glob(path2 + category[0]))
dog_path = sorted(glob.glob(path2 + category[1]))
pig_path = sorted(glob.glob(path2 + category[2]))


''' Convert RGB image to GRAY '''


def gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


def dodge(front, back):
    result = front*255 / (255 - back + 1)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')


''' Calculate Image Histogram'''


def image_analysis():
    img_human = (cv.imread(path))
    img_cat = (cv.imread(cat_path))
    img_dog = (cv.imread(dog_path))
    img_pig = (cv.imread(pig_path))
    img_human = cv.resize(img_human, (256, 256))

    img_human_his = gray(img_human)
    img_cat_his = gray(img_cat)
    img_dog_his = gray(img_dog)
    img_pig_his = gray(img_pig)

    # Gaussian filtering
    human_gauss = scipy.ndimage.filters.gaussian_filter(255-img_human_his, 300)
    cat_gauss = scipy.ndimage.filters.gaussian_filter(255-img_cat_his, 300)
    dog_gauss = scipy.ndimage.filters.gaussian_filter(255-img_dog_his, 300)
    pig_gauss = scipy.ndimage.filters.gaussian_filter(255-img_pig_his, 300)

    # Calculate Dodge image
    human_dodge = cv.equalizeHist(dodge(human_gauss, img_human_his))  # Must be grayscale
    cat_dodge = cv.equalizeHist(dodge(cat_gauss, img_cat_his))
    dog_dodge = cv.equalizeHist(dodge(dog_gauss, img_dog_his))
    pig_dodge = cv.equalizeHist(dodge(pig_gauss, img_pig_his))

    # Calculate pixel-wise score
    cat_err = np.sum((human_dodge.astype("float") - cat_dodge.astype("float")) ** 2)
    cat_err /= float(human_dodge.shape[0] * human_dodge.shape[1])
    cat_ssim = ssim(human_dodge, cat_dodge)

    dog_err = np.sum((human_dodge.astype("float") - dog_dodge.astype("float")) ** 2)
    dog_err /= float(human_dodge.shape[0] * human_dodge.shape[1])
    dog_ssim = ssim(human_dodge, dog_dodge)

    pig_err = np.sum((human_dodge.astype("float") - pig_dodge.astype("float")) ** 2)
    pig_err /= float(human_dodge.shape[0] * human_dodge.shape[1])
    pig_ssim = ssim(human_dodge, pig_dodge)

    # Get error
    min_error = min(cat_err, dog_err, pig_err)
    label = (lambda n, m, k: 'Cat' if(n == min_error) else 'Dog' if(m == min_error) else 'Pig')(cat_err, dog_err, pig_err)

    # Calculate & Compare histogram
    hist_human = cv.calcHist([img_human], [1], None, [256], [0, 256])
    hist_cat = cv.calcHist(img_cat, [1], None, [256], [0, 256]) * 100
    hist_dog = cv.calcHist(img_dog, [1], None, [256], [0, 256]) * 100
    hist_pig = cv.calcHist(img_pig, [1], None, [256], [9, 256]) * 100

    f, axes = plt.subplots(2, 2, figsize=(8, 6), sharex=True)
    sns.distplot(hist_human, color="y", axlabel=label, ax=axes[0, 0]), plt.xlim([0, 2000])
    sns.distplot(hist_cat, color="r", axlabel="Cat_face", ax=axes[0, 1]),  plt.xlim([0, 2000])
    sns.distplot(hist_dog, color="b", axlabel="Dog_face", ax=axes[1, 0]),  plt.xlim([0, 2000])
    sns.distplot(hist_pig, color="g", axlabel="Pig_face", ax=axes[1, 1]),  plt.xlim([0, 2000])

    plt.savefig('/home/mlpa/PycharmProjects/KJW/capstone_project/human2animal/transfer_network/image_transfer/test_transfer/plot/plot%04d.png'%(i))
    plt.close()
