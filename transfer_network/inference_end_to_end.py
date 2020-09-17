import io
import json
import torch
import cv2 as cv
import numpy as np
import torchvision.transforms as transforms

from PIL import Image
from torchvision.utils import save_image
from skimage.measure import _structural_similarity

from transfer_network.cycleGAN_model import Generator
from transfer_network.blending import blending

animal_class_index = json.load(open('../transfer_network/animal_class_index.json'))
ssim = _structural_similarity.compare_ssim
path = '/home/mlpa/CapstoneServer/transfer_network'

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def get_prediction(image_bytes):

    make_fake(image_bytes=image_bytes)
    cat_ssim, dog_ssim, pig_ssim, bear_ssim = classification(image_bytes)

    score = max(cat_ssim, dog_ssim, pig_ssim, bear_ssim)

    if score == cat_ssim:
        predicted_idx = str(0)
        blending('cat')
    elif score == dog_ssim:
        predicted_idx = str(1)
        blending('dog')
    elif score == pig_ssim:
        predicted_idx = str(2)
        blending('pig')
    else:
        predicted_idx = str(3)
        blending('bear')

    return animal_class_index[predicted_idx], cat_ssim, dog_ssim, pig_ssim, bear_ssim


def transform_image(image_bytes):
    
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.22])])
    image = Image.open(io.BytesIO(image_bytes))
    image.save('/home/mlpa/CapstoneServer/transfer_network/cache/human_original.jpg')
    return my_transforms(image).unsqueeze(0)


def make_fake(image_bytes):

    input_image = transform_image(image_bytes=image_bytes)
    input_image = input_image.to(device)

    cat_netG_B2A = Generator(3, 3)
    dog_netG_B2A = Generator(3, 3)
    pig_netG_B2A = Generator(3, 3)
    bear_netG_B2A = Generator(3, 3)

    cat_netG_B2A.to(device)
    dog_netG_B2A.to(device)
    pig_netG_B2A.to(device)
    bear_netG_B2A.to(device)

    # Load state dicts
    cat_netG_B2A.load_state_dict(torch.load(path + '/network_cat/cat_netG_A2B.pth'))
    dog_netG_B2A.load_state_dict(torch.load(path + '/network_dog/dog_netG_A2B.pth'))
    pig_netG_B2A.load_state_dict(torch.load(path + '/network_pig/pig_netG_A2B.pth'))
    bear_netG_B2A.load_state_dict(torch.load(path + '/network_bear/bear_netG_A2B.pth'))

    # Set model's test mode
    cat_netG_B2A.eval()
    dog_netG_B2A.eval()
    pig_netG_B2A.eval()
    bear_netG_B2A.eval()

    # Generate output
    fake_cat = 0.5 * (cat_netG_B2A(input_image) + 1.0)
    fake_dog = 0.5 * (dog_netG_B2A(input_image) + 1.0)
    fake_pig = 0.5 * (pig_netG_B2A(input_image) + 1.0)
    fake_bear = 0.5 * (bear_netG_B2A(input_image) + 1.0)

    save_image(fake_cat, path + '/cache/human_cat.jpg')
    save_image(fake_dog, path + '/cache/human_dog.jpg')
    save_image(fake_pig, path + '/cache/human_pig.jpg')
    save_image(fake_bear, path + '/cache/human_bear.jpg')


def classification(image_bytes):
    
    pic_human = Image.open(io.BytesIO(image_bytes))
    pic_human = np.array(pic_human)

    pic_cat = path + '/cache/human_cat.jpg'
    pic_dog = path + '/cache/human_dog.jpg'
    pic_pig = path + '/cache/human_pig.jpg'
    pic_bear = path + '/cache/human_bear.jpg'

    # Read Image
    img_human = cv.resize(pic_human, (224, 224))
    img_cat = cv.imread(pic_cat)
    img_dog = cv.imread(pic_dog)
    img_pig = cv.imread(pic_pig)
    img_bear = cv.imread(pic_bear)

    # Canny algorithm
    human_gray = cv.cvtColor(img_human, cv.COLOR_BGR2GRAY)
    cat_gray = cv.cvtColor(img_cat, cv.COLOR_BGR2GRAY)
    dog_gray = cv.cvtColor(img_dog, cv.COLOR_BGR2GRAY)
    pig_gray = cv.cvtColor(img_pig, cv.COLOR_BGR2GRAY)
    bear_gray = cv.cvtColor(img_bear, cv.COLOR_BGR2GRAY)

    human_edges = cv.Canny(human_gray, 170, 190)
    cat_edges = cv.Canny(cat_gray, 170, 190)
    dog_edges = cv.Canny(dog_gray, 170, 190)
    pig_edges = cv.Canny(pig_gray, 170, 190)
    bear_edges = cv.Canny(bear_gray, 170, 190)

    cat_err = np.sum((human_edges.astype("float") - cat_edges.astype("float")) ** 2)
    cat_err /= float(human_edges.shape[0] * human_edges.shape[1])
    cat_ssim = ssim(human_edges, cat_edges)

    dog_err = np.sum((human_edges.astype("float") - dog_edges.astype("float")) ** 2)
    dog_err /= float(human_edges.shape[0] * human_edges.shape[1])
    dog_ssim = ssim(human_edges, dog_edges)

    pig_err = np.sum((human_edges.astype("float") - pig_edges.astype("float")) ** 2)
    pig_err /= float(human_edges.shape[0] * human_edges.shape[1])
    pig_ssim = ssim(human_edges, pig_edges)

    bear_err = np.sum((human_edges.astype("float") - bear_edges.astype("float")) ** 2)
    bear_err /= float(human_edges.shape[0] * human_edges.shape[1])
    bear_ssim = ssim(human_edges, bear_edges)

    return cat_ssim, dog_ssim, pig_ssim, bear_ssim
