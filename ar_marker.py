import cv2
import os


class ar_marker(object):
    def __init__(self):
        
        # Path to the image
        self.path = "ar_testing/"

        # Path to save
        self.save_path = "results/"

        # Create a sift feature extractor
        self.featured = cv2.xfeatures2d.SIFT_create()

        self.feature_detection()
        # self.feature_match()



    def feature_detection(self):
        
        # Reading the image
        image = cv2.imread(self.path + "set_1/img01.jpg")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect features from the image
        keypoints, descriptors = self.featured.detectAndCompute(image, None)

        # Draw the detected key points
        featured_image = cv2.drawKeypoints(gray, keypoints, image)
        
        # Save image
        cv2.imwrite(self.save_path + "img01_keypoints.jpg", featured_image)



    def feature_match(self):
        
        # Reading the images
        image1 = cv2.imread(self.path + "set_1/book_cover_1.jpg")
        image2 = cvs.imread(self.path + "set_2/book_cover_2.jpg")

        









if __name__ == "__main__":
   

    # ar_markers make object
    ar_marker_obj = ar_marker()




