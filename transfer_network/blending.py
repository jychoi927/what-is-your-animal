import cv2
import matplotlib.pyplot as plt

path = '/home/mlpa/CapstoneServer/transfer_network'


def blending(name):
    human_in = cv2.imread(path + '/cache/human_original.jpg', cv2.IMREAD_COLOR)

    if name is 'cat':
        animal_in = cv2.imread(path + '/cache/human_cat.jpg', cv2.IMREAD_COLOR)
    elif name is 'dog':
        animal_in = cv2.imread(path + '/cache/human_dog.jpg', cv2.IMREAD_COLOR)
    elif name is 'pig':
        animal_in = cv2.imread(path + '/cache/human_pig.jpg', cv2.IMREAD_COLOR)
    elif name is 'bear':
        animal_in = cv2.imread(path + '/cache/human_bear.jpg', cv2.IMREAD_COLOR)
    else:
        print("Error occurs.")

    human = cv2.cvtColor(human_in, cv2.COLOR_BGR2RGB)
    animal = cv2.cvtColor(animal_in, cv2.COLOR_BGR2RGB)

    human = cv2.resize(human, (225, 225))
    animal = cv2.resize(animal, (225, 225))

    img0 = cv2.addWeighted(human, float(100 - 0) / 100, animal, float(0) / 100, 0)
    img1 = cv2.addWeighted(human, float(100 - 33) / 100, animal, float(33) / 100, 0)
    img2 = cv2.addWeighted(human, float(100 - 66) / 100, animal, float(66) / 100, 0)
    img3 = cv2.addWeighted(human, float(100 - 100) / 100, animal, float(100) / 100, 0)

    plt.imsave('/home/mlpa/CapstoneServer/FlaskAPP/static/cache/human+animal_img0.png', img0)  # human:animal = 100:0
    plt.imsave('/home/mlpa/CapstoneServer/FlaskAPP/static/cache/human+animal_img1.png', img1)  # human:animal = 67:33
    plt.imsave('/home/mlpa/CapstoneServer/FlaskAPP/static/cache/human+animal_img2.png', img2)  # human:animal = 34:66
    plt.imsave('/home/mlpa/CapstoneServer/FlaskAPP/static/cache/human+animal_img3.png', img3)  # human:animal = 0:100
