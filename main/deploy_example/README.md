# Basics of Model Training and Web App Deploy

This example set of code is meant to show a simple approach to training a classifier model and using streamlit + FastAPI to host the model as a web app, allowing a user to input data and get a prediction. Below are two links to video tutorials that...

1. [Describe the model training process](https://drive.google.com/file/d/1ov0AOGJrEjI6J6z6SUEnuLIu0Ii8mdba/view?usp=sharing) and...
2. [Demonstrate the web app](https://drive.google.com/file/d/1g9Pucm3wM8P_AUttxUIb8rYr7Jf6ipYJ/view?usp=sharing)

Please note that the development of this model is prototyping level only. Production level model development would involve deeper exploratory data analysis, training exercises, performance metrics, optimizations, etc. The same is true of the use of the term "deploy" here. This project is meant to showcase a toy example for how user input can be passed to a pre-trained model, return predictions, and some of the safety checks developers should be aware of. This doesn't require the same level of monitoring, versioning, and data pipeline integration that would be needed for deploying a model in a larger, production level software application.