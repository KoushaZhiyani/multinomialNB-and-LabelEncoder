# multinomialNB-and-LabelEncoder
<h3>LabelEncoder</h3>
Label encoding is a technique used in machine learning and data analysis to convert categorical variables into numerical format.<br>

To use the LabelEncoder class, you can follow these steps:<br>
Import Libraries:<br>
```import pandas as pd```<br>
Instantiate the Encoder: Create an instance of the label_encoder class.<br>
```encoder = label_encoder()```<br>
Train the Encoder:```encoder.train(train_data)```<br>
Transform Data: Once trained, you can use the encoder to transform new data into encoded form. <br>
```encoded_data = encoder.transform(test_data)```<br>

<br>
<h3>multinomialNB</h3>

The Multinomial Naive Bayes algorithm is a Bayesian learning approach popular in Natural Language Processing (NLP). The program guesses the tag of a text, such as an email or a newspaper story, using the Bayes theorem.<br>

To use the NBMultinomial class, you can follow these steps:<br>
Import Libraries:<br>
```import pandas as pd```<br>
Instantiate the Encoder: Create an instance of the label_encoder class.<br>
```classifier = NBMultinomial()``` <br>
Train the Classifier: Train the classifier with your training data.<br>
```
 X_train = pd.DataFrame(...) 
    y_train = pd.Series(...)    
    classifier.train_data(X_train, y_train)
```
<br>
Make Predictions: Use the trained classifier to make predictions on new data. 

```
X_test = pd.DataFrame(...)  
predictions = classifier.predict(X_test)
```

<br>
Evaluate the Model: Optionally, you can evaluate the performance of your model using the score method. 

```true_labels = pd.Series(...)  
accuracy = NBMultinomial.score(predictions, true_labels)
```



