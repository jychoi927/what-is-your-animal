import cv2 as cv
import numpy as np
from skimage.measure import _structural_similarity

ssim = _structural_similarity.compare_ssim
path = '/home/mlpa/CapstoneServer/transfer_network/image_transfer/test_transfer/'
category = ['cat', 'dog', 'pig']  # 1. cat, 2. dog, 3. pig

cat_path = path + category[0]
dog_path = path + category[1]
pig_path = path + category[2]

for i in range(1, 12):

    pic_human = '/home/mlpa/CapstoneServer/transfer_network/image_transfer/test_human/human_%04d.jpg' % i
    pic_cat = cat_path + '/human_cat_%04d.jpg' % i
    pic_dog = dog_path + '/human_dog_%04d.jpg' % i
    pic_pig = pig_path + '/human_pig_%04d.jpg' % i

    # Read Image
    img_human = cv.imread(pic_human)
    img_human = cv.resize(img_human, (256, 256))
    img_cat = cv.imread(pic_cat)
    img_dog = cv.imread(pic_dog)
    img_pig = cv.imread(pic_pig)

    # Canny algorithm
    human_gray = cv.cvtColor(img_human, cv.COLOR_BGR2GRAY)
    cat_gray = cv.cvtColor(img_cat, cv.COLOR_BGR2GRAY)
    dog_gray = cv.cvtColor(img_dog, cv.COLOR_BGR2GRAY)
    pig_gray = cv.cvtColor(img_pig, cv.COLOR_BGR2GRAY)

    human_edges = cv.Canny(human_gray, 170, 190)
    cat_edges = cv.Canny(cat_gray, 170, 190)
    dog_edges = cv.Canny(dog_gray, 170, 190)
    pig_edges = cv.Canny(pig_gray, 170, 190)

    cv.imwrite('/home/mlpa/CapstoneServer/transfer_network/image_transfer/edge_result/cat/cat_%04d.jpg' % i, 
               cat_edges)
    cv.imwrite('/home/mlpa/CapstoneServer/transfer_network/image_transfer/edge_result/dog/dog_%04d.jpg' % i, 
               dog_edges)
    cv.imwrite('/home/mlpa/CapstoneServer/transfer_network/image_transfer/edge_result/pig/pig_%04d.jpg' % i, 
               pig_edges)
    cv.imwrite('/home/mlpa/CapstoneServer/transfer_network/image_transfer/edge_result/human/human_%04d.jpg' % 
               i, human_edges)

    human = np.asarray(human_edges)
    cat = np.asarray(cat_edges)
    dog = np.asarray(dog_edges)
    pig = np.asarray(pig_edges)

    cat_err = np.sum((human_edges.astype("float") - cat_edges.astype("float"))**2)
    cat_err /= float(human_edges.shape[0] * human_edges.shape[1])
    cat_ssim = ssim(human_edges, cat_edges)

    dog_err = np.sum((human_edges.astype("float") - dog_edges.astype("float"))**2)
    dog_err /= float(human_edges.shape[0] * human_edges.shape[1])
    dog_ssim = ssim(human_edges, dog_edges)

    pig_err = np.sum((human_edges.astype("float") - pig_edges.astype("float"))**2)
    pig_err /= float(human_edges.shape[0] * human_edges.shape[1])
    pig_ssim = ssim(human_edges, pig_edges)

    print("The MSE of %04dth cat is : %f" % (i, cat_err))
    print("The MSE of %04dth dog is : %f" % (i, dog_err))
    print("The MSE of %04dth pig is : %f\n" % (i, pig_err))
    print("The SSIM of %04dth cat is : %f" % (i, cat_ssim))
    print("The SSIM of %04dth dog is : %f" % (i, dog_ssim))
    print("The SSIM of %04dth pig is : %f" % (i, pig_ssim))

    score = max(cat_ssim, dog_ssim, pig_ssim)

    if score == cat_ssim:
        print("This person looks like... a cat\n\n\n")
    elif score == dog_ssim:
        print("This person looks like... a dog\n\n\n")
    else:
        print("This person looks like... a pig\n\n\n")
