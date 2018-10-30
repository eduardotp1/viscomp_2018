# import cv2
import os
# import numpy as np
# from random import shuffle
# import pickle
# from gluoncv import model_zoo, data, utils
# from matplotlib import pyplot as plt
# import argparse

# def compute_descriptors(image):
#     img = cv2.imread(image,0)
#     surf = cv2.xfeatures2d.SURF_create(hessianThreshold=400, extended=True, upright=True)#300-500
#     kp, des = surf.detectAndCompute(img,None)
#     return kp, des

# def read_image_descriptors(path, folders, max_items=5):
#     paths = []
#     descriptors = []
#     for folder in folders:
#         directory = sorted(os.listdir(path + folder))
#         shuffle(directory)
#         images = [f for f in directory if not f.startswith('.')][:max_items]
#         for img in images:
#             imgout = path + folder + "/" + img
#             kp, des = compute_descriptors(imgout)
#             descriptors.append(des)
#             paths.append(imgout)
#     return paths, np.vstack(descriptors)

# def create_vocabulary(desc, sz=300):
#     kmeans = KMeans(n_clusters=sz, random_state=0).fit(desc)
#     return (kmeans.cluster_centers_, kmeans)

# def draw_histogram(image, vocab):
#     kp, desc = compute_descriptors(image)
#     centers, kmeans = vocab
#     closest = kmeans.predict(desc)
    
#     hist = np.ones(centers.shape[0])
#     for e in closest:
#         hist[e]+=1
#     return hist

# def compare_histograms(hist, hist_vocab):
#     return chisquare(hist, f_exp = hist_vocab)[0]

# def create_vocab_hists(paths, vocab):
#     vocab_hists = []
#     for e in paths:
#         h = draw_histogram(e, vocab)
#         vocab_hists.append((e, h))
#     return vocab_hists

# def find_similar_bvw(image, vocab, vocab_hists, show=False):
#     hist = draw_histogram(image, vocab)
    
#     distances = []
#     for vocab_h in vocab_hists:
#         chi_squared = compare_histograms(hist, vocab_h[1])
#         distances.append((vocab_h[0], chi_squared))
        
#     sorted_distances = sorted(distances, key=lambda x: x[1], reverse=False)[:3]
#     img1 = cv2.imread(image,0)
#     print("Search Image:", image)
#     if (show == True):
#         plt.imshow(img1, cmap="gray")
#         plt.title("Search Image")
#         plt.show()
#     for match in sorted_distances:
#         print("Found Image:", match[0])
#         if (show == True):
#             print("Chi_Squared:", match[1])
#             img2 = cv2.imread(match[0],0)
#             plt.imshow(img2, cmap="gray")
#             plt.title("Found Image")
#             plt.show()
#         print("--------------")

# ################################################

# #Treinar
# def train(test_path, folders, max_items=15):
#     if not os.path.exists('./helper/'):
#         os.makedirs('./helper/')
#     print("Begin training...")
#     paths, image_descriptors = read_image_descriptors(test_path, folders, max_items)
#     print("Creating vocabulary...")
#     vocab = create_vocabulary(image_descriptors)
#     print("Dumping into pickle...")
#     pickle.dump(vocab, open("./helper/vocab.p", "wb"))
#     print("Computating vocabulary histograms...")
#     vocab_hists = create_vocab_hists(paths, vocab)
#     print("Dumping into pickle...")
#     pickle.dump(vocab_hists, open("./helper/vocab_hists.p", "wb"))
#     print("Finished sucessfully!")

# #Procurar
# def find(image, show=False):
#     if not os.path.exists('./helper/'):
#         print("ERROR: 'helper' folder does not exist!")
#         print("Write -h or --help for more information.")
#         exit(1)
#     vocab = pickle.load(open("./helper/vocab.p", "rb"))
#     vocab_hists = pickle.load(open("./helper/vocab_hists.p", "rb"))
#     find_similar_bvw(image, vocab, vocab_hists, show)

def main():
    paths = []
    dataset = "dataset-projeto-3-2/"
    folders = os.listdir(dataset)
    for folder in folders:
        images = os.listdir(dataset + folder)
        temp = [dataset + folder + "/" + f for f in images]
        for p in temp:
            paths.append(p)
    print(paths[0])
    

#     parser = argparse.ArgumentParser(description='Given a term, return the top 3 most similar images in the database.')
#     parser.add_argument('keyword', type=str, help='Keyword for search')
#     args = parser.parse_args()
#     find(args.path, show=args.show)

if __name__ == '__main__':
    main()