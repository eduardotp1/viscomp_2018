import cv2
import os
from matplotlib import pyplot as plt
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input, decode_predictions, MobileNet
import numpy as np
import pickle
import argparse

def get_all_image_paths(dataset):
    paths = []
    folders = os.listdir(dataset)
    for folder in folders:
        images = os.listdir(dataset + folder)
        temp = [dataset + folder + "/" + f for f in images]
        for p in temp:
            paths.append(p)
    return paths

def mnetv2_loadimage(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return preprocess_input(x)

def image_classification(paths):
    classification_dict = {}
    model = MobileNet(input_shape=None, alpha=1.0, depth_multiplier=1, include_top=True, weights='imagenet', input_tensor=None, pooling=None, classes=1000)
    for path in paths:
        image = mnetv2_loadimage(path)
        preds = model.predict(image)
        prediction = decode_predictions(preds, top=1)[0][0]
        img_class = prediction[1]
        img_confidence = prediction[2]
        if img_class in classification_dict:
            classification_dict[img_class].append((path, img_confidence))
        else:
            classification_dict[img_class] = [(path, img_confidence)]
    return classification_dict

#Treinar
def train(dataset="dataset-projeto-3-2/"):
    if not os.path.exists('./helper/'):
        os.makedirs('./helper/')
    print("Begin training...")
    print("Getting all image paths...")
    paths = get_all_image_paths(dataset)
    print("Creating dict with paths...")
    classification = image_classification(paths)
    print(classification)
    print("Dumping into pickle...")
    pickle.dump(classification, open("./helper/dict.p", "wb"))
    print("Finished sucessfully!")

def greaterless(a, b):
    if a > b:
        return b
    else:
        return a

def show_images(term, classifications, show=False):
    print("Term used:", term)
    match = classifications.get(term)
    sorted_by_trust = sorted(match, reverse=True, key=lambda tup: tup[1])
    size = greaterless(5, len(sorted_by_trust))
    for i in range(size):
        print("Path to Image: ", sorted_by_trust[i][0])
        print("Score: ", sorted_by_trust[i][1])
        if (show == True):
            img = cv2.imread(sorted_by_trust[i][0], 1)
            plt.imshow(img)
            plt.title("Matched Image")
            plt.show()
        print("--------------")


#Procurar
def find(term, show=False):
    if not os.path.exists('./helper/'):
        print("ERROR: 'helper' folder does not exist!")
        print("Write -h or --help for more information.")
        exit(1)
    paths_dict = pickle.load(open("./helper/dict.p", "rb"))

    if term in paths_dict:
        show_images(term, paths_dict, show)
    else:
        print("ERROR: used term '" + term + "' not valid.")
        print("Please use these terms instead: https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a")
        print("Write -h or --help for more information.")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='Given a term, return the top 5 most similar images in the database.')
    parser.add_argument('keyword', type=str, help='Keyword for search')
    parser.add_argument('-s', '--show', action='store_true', help='Shows the 5 images instead of returning the path')
    parser.add_argument('-t', '--train', action='store_true', help='Returns pickle objects in "helper" folder')
    args = parser.parse_args()
    if (args.train == True):
        train(args.keyword)
    else:
        find(args.keyword, show=args.show)

if __name__ == '__main__':
    main()