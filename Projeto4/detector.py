import cv2
import cv2.aruco as aruco
import numpy as np
import argparse

def augment_reality(path):
    #Load reference image and replacement image
    replacement_img = cv2.imread(path)
    board_img = cv2.imread("board_aruco.png")

    #Detect markers in reference image and get origin points
    board_img_gray = cv2.cvtColor(board_img, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
    board_markers, board_ids, _ = aruco.detectMarkers(board_img_gray, aruco_dict, parameters=parameters)
    orig_points = np.asarray(board_markers).reshape((-1,2))

    # Using webcam
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read() #640x480
        frame_copy = frame.copy()

        # Detecting markers in real time
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters =  aruco.DetectorParameters_create()
        markers, ids, _ = aruco.detectMarkers(gray_image, aruco_dict, parameters=parameters)

        if (len(markers) == 0):
            print("Nenhum marcador encontrado.")
        else:
            dest_points = np.asarray(markers).reshape((-1,2))

            # Find the reference coordinate of the detected markers
            ids = np.asarray(ids)
            detected_orig_points = []
            for id in ids:
                index = np.argwhere(board_ids == id)[0][0]
                for i in range(4):
                    detected_orig_points.append(orig_points[(index*4)+i])
            detected_orig_points = np.asarray(detected_orig_points).astype(int)

            # Black image with replacement image over markers
            homography = cv2.findHomography(detected_orig_points, dest_points)[0]
            h, w, _ = frame.shape
            warped_image = cv2.warpPerspective(replacement_img, homography, (w, h), frame_copy)

            # Optional -- draw detected markers in image
            # aruco.drawDetectedMarkers(frame, markers)

            # Overlapping images
            mask = warped_image > [0, 0, 0]
            frame = np.where(mask == True, warped_image, frame)

        # Show image, press q to exit
        cv2.imshow('clean image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean everything up
    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description='Replace aruco markers image with another image of your choice.')
    parser.add_argument('path', type=str, help='Path to replacement image')
    args = parser.parse_args()
    augment_reality(args.path)

if __name__ == '__main__':
    main()