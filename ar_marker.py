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

        # Create feature matcher
        self.feature_matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

        self.feature_detection()
        self.feature_match()



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
        image2 = cv2.imread(self.path + "set_2/book_cover_3.jpg")


        # Convert image 1
        gray_1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray_2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        

        # Detect features from the image
        keypoints_1, descriptors_1 = self.featured.detectAndCompute(image1, None)
        keypoints_2, descriptors_2 = self.featured.detectAndCompute(image2, None)


        # Match descriptors of both images
        image_matches = self.feature_matcher.match(descriptors_1, descriptors_2)

        # Sort matches by distance
        matches = sorted(image_matches, key = lambda x:x.distance)

        print("matches", len(matches))


        matched_image = cv2.drawMatches(image1, keypoints_1, image2, keypoints_2, matches[:400], image2, flags=2)

        # Save image
        cv2.imwrite(self.save_path + "book_matched_image_2.jpg", matched_image)






    def load_image(self):
        pass




    def save_images(self):
        pass




    # Compare modified ar marker
    def compare_diffrence(self):
        pass

        



if __name__ == "__main__":
   

    # Ar markers make object
    ar_marker_obj = ar_marker()




