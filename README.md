# Monitoring-Human-Movements-and-Automated-Alert-System-for-Suspicious-Behaviour-using-LSTM-Model

Falls among the elderly pose serious risks, including injuries and even death. To address this concern, a system utilizes a Long Short-Term Memory (LSTM) model for human fall detection. By leveraging OpenCV and Openpifpaf, the system performs keypoint recognition on body parts, enabling detailed analysis of human movements and accurate identification of falls. When a fall is detected, the system sends an SMS alert to a designated guardian or caretaker using Twilio. The system is also capable of recognizing other activities like walking, running, and sitting, and can be easily customized for additional activities. This affordable and non-intrusive solution proves beneficial in various settings, including nursing homes, hospitals, and private homes. By promptly notifying guardians or caretakers of falls, the system helps reduce the risk of injury and improves the safety and well-being of elderly individuals.

# Dataset

https://sites.google.com/up.edu.mx/har-up/

The HAR (Human Activity Recognition) dataset is a widely used dataset for machine learning research in the field of human activity recognition. The HAR dataset consists of sensor data collected from smartphones worn by17 human subjects while they perform various activities, such as walking, jogging, sitting, and standing. This dataset is publicly available, and it comprises 11 activities performed by 17 subjects during 3 attempts each.

The organization of the dataset is as follows:
* 17-folders, one per subject.
* 11-subfolders, one per activity.
* 3 - subfolders, one per trial.
* 1-CSV file containing the sensor signals of the attempt
 
A Python script is used to download and process a dataset for human activity recognition. The script fetches the dataset from a webpage, extracts information about cases, activities, and trials using regular expressions, and creates a folder to store the downloaded data. It iterates over each case and activity, downloads a zip file containing image sequences, extracts the images, and saves them in a new directory. The script then utilizes the ffmpeg library to convert the image sequences into video files with a frame rate of 18 frames per second. These resulting video files can be used to train and test models for human activity recognition. The script employs Python packages such as re, requests, BeautifulSoup, gdown, zipfile, shutil, and os for downloading, extracting, and processing the image files. This code provides a convenient solution for accessing and analyzing datasets used in various domains like healthcare, sports, and security.

# Modules
* Pytorch
* torch.nn
* torch.multiprocessing
* openpifpaf
* pillow
* numpy
* pandas
* cv2
* matplotlib
