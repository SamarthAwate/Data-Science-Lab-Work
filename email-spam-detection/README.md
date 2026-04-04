Description

The objective of this project is to classify emails as spam or not spam using machine learning techniques. 
The model is trained on labeled email data and uses text preprocessing and feature extraction to make predictions.

Dataset
Source: Kaggle (SMS Spam Collection Dataset)
Description of data:
The dataset contains labeled messages categorized as "spam" or "ham" (not spam). Each entry includes the message text and its corresponding label.

Steps Performed
Data Cleaning
Removed special characters, converted text to lowercase, and removed stopwords.
Exploratory Data Analysis
Analyzed the distribution of spam vs non-spam messages.
Visualization
Created bar charts to visualize class distribution.
Model Building
Used TF-IDF for feature extraction and trained a Naive Bayes classifier.

Results
Accuracy: 97.9%
Precision: 99.2%
Recall: 85.3%
F1 Score: 91.7%

The model performs very well overall, with high accuracy and precision. However, recall is slightly lower, indicating that some spam messages are not detected.

Tools Used
Python
Libraries:
Pandas
NumPy
Scikit-learn
NLTK
Matplotlib

Conclusion

This project demonstrates how machine learning can be applied to text classification problems. With proper preprocessing and feature extraction, models like Naive Bayes can effectively detect spam messages.

Author

Samarth Awate
