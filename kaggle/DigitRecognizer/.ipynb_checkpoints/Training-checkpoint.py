from sklearn.externals import joblib
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy as np

class Training:
    def creat_model(self):
        dataset = datasets.fetch_mldata("MNIST Original")
        features = np.array(dataset.data, 'int16')
        labels = np.array(dataset.target, 'int')
        list_hog_fd = []
        for feature in features:
            fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1),
                     visualise=False)
            list_hog_fd.append(fd)
            hog_features = np.array(list_hog_fd, 'float64')
            print("Cleaning...")
        clf = LinearSVC()
        clf.fit(hog_features, labels)
        joblib.dump(clf, "digits_cls.pkl", compress=3)
        print("MOdels Savved")

if __name__ == "__main__":
    obj = Training()
    obj.creat_model()


