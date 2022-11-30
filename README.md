# Predictive modelling for hit songs audio features for choruses
[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org)

## About
This project aims to predict if a certain song will hit(get popular) or not, and thus will be depending on the features extracted from audio songs.

## Project details
### 1. Extract the popular and unpopular songs from billboard websit:
Here, I have tried for the first time to make a web scraping, where I have extracted the hot 100 songs and saving them into a csv file. [BillBoard_web_scraping.ipynb](https://github.com/Nourhan-Adell/Data_Science_Projects/blob/main/BillBoard_web_scraping.ipynb)
After that I have used the billboard API to extract more needed features from the websit. [Collecting_Billboard_Data.ipynb](https://github.com/Nourhan-Adell/Data_Science_Projects/blob/main/Collecting_Billboard_Data.ipynb)

### 2. Downloading songs:
I have downloaded the audio files from youtube and save them into a csv file with needed informayion. [Downloading_Music_Files.ipynb](https://github.com/Nourhan-Adell/Data_Science_Projects/blob/main/Downloading_Music_Files.ipynb)

### 3. Extract chorus:
In this part I have looped on all the songs either popular or unpopular and start to extract the most useful chorus of 15 seconds. [Extract_Chorus.ipynb](https://github.com/Nourhan-Adell/Data_Science_Projects/blob/main/Extract_Chorus.ipynb)

### 4. Extract audio features:
The major features that are extracted are : (chroma_stft, chroma_cqt, chroma_cens, mfcc, rms, spectral_centroid, spectral_bandwidth, spectral_contrast, spectral_rolloff, tonnetz, zero_crossing_rate). [Extract_audio_features.ipynb](https://github.com/Nourhan-Adell/Data_Science_Projects/blob/main/Extract_audio_features.ipynb)

### 5. Applying The model:
Here, I have applied the best model accuracy to this data which is the Decision tree model which has the best accuracy 58%. [MusicData_DecisionTree.ipynb](https://github.com/Nourhan-Adell/Data_Science_Projects/blob/main/6.%20MusicData_DecisionTree.ipynb)

And finally I have prepared the .pkl file to be ready for deployment.
### 6. Deployment of the model:
We have deployed the model by using flask, where the webpage asks the user to write song's link and then predict if it will be popular one or not.

![](Demo.mp4)
