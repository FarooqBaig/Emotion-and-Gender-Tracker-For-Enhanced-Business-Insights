# Emotion-and-Gender-Tracker-For-Enhanced-Business-Insights

This repository contains code for emotion and gender tracking in images and videos. The implementation utilizes individual CNN architecture models for emotion detection and gender classification. The detected emotions and genders are stored for later tracking and analysis. The project includes the use of Haar cascade classifier, Python, Keras, TensorFlow, OpenCV, and Streamlit.

**Requirements**

To run the emotion and gender tracker, you need to have the following dependencies installed:

1. Python (version 3.6 or higher)

2. OpenCV (version 4.0 or higher)

3. NumPy

4. TensorFlow (version 2.0 or higher)

5. Keras (version 2.0 or higher)
 
6. Streamlit

7. Haar Cascade Classifier

The Haar cascade classifier is utilized for face detection in the input images and videos. It is implemented using the OpenCV library. The pre-trained Haar cascade model detects faces and extracts the facial region, which is then used for emotion detection and gender classification.

**Emotion Detection CNN Model**

The emotion detection model is based on a CNN architecture. It is trained on a dataset such as FER-2013, which contains images of faces labeled with different emotions. The trained model is used to classify emotions from the facial images.

**Gender Classification CNN Model**

The gender classification model also uses a CNN architecture. It is trained on a dataset with labeled images of male and female faces. The trained model is used to classify the gender of the detected faces.

![image](https://github.com/FarooqBaig/Emotion-and-Gender-Tracker-For-Enhanced-Business-Insights/assets/74425452/db3c79f5-0122-47a9-b2b0-eaf030e249a8)


**Data Storage and Tracking**

The detected emotions and genders are stored for each image or video frame processed using SQLite Database. This allows for later analysis and tracking of the emotions and genders of individuals. The storage can be implemented using a database or a simple file system.

**Streamlit Application**

The Streamlit application provides a user interface to interact with the emotion and gender tracker. It allows users to upload images or videos, and it displays the tracked emotions and genders in real-time. The Streamlit application is implemented in a separate Python file, tracker_app.py.

**Usage**

Install the required dependencies mentioned above.

Clone this repository to your local machine.

Ensure that you have the necessary datasets available for training the emotion detection and gender classification models.

Run the tracker_app.py script to start the Streamlit application.

```
streamlit run Home.py
```
Access the Streamlit application in your web browser at the provided local URL.

Upload images or videos to the application and observe the real-time emotion and gender tracking results.

![image](https://github.com/FarooqBaig/Emotion-and-Gender-Tracker-For-Enhanced-Business-Insights/assets/74425452/10351089-352b-4753-a452-5f79c58d3732)

![image](https://github.com/FarooqBaig/Emotion-and-Gender-Tracker-For-Enhanced-Business-Insights/assets/74425452/c1943628-85b1-4a9c-b031-c10e9f54a436)

![image](https://github.com/FarooqBaig/Emotion-and-Gender-Tracker-For-Enhanced-Business-Insights/assets/74425452/ca667c8c-dd8b-427c-ab1d-7156543b9733)



