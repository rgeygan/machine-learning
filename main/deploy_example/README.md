# Basics of Model Training and Web App Deploy

This example set of code is meant to show a simple approach to training a classifier model and using streamlit + FastAPI to host the model as a web app, allowing a user to input data and get a prediction. There are two links to video tutorials in this directory that 

1. [Describe the model training process](https://drive.google.com/file/d/1ov0AOGJrEjI6J6z6SUEnuLIu0Ii8mdba/view?usp=sharing) and...
2. Demonstrate the web app

Please note that the development of this model is prototyping level only. Production level model development would involve much more EDA, training exercises, performance metrics, optimizations, etc. The same is true of my use of the term "deploy" here. This project is meant to showcase a toy example for how user input can be passed to a pre-trained model and return predictions. This doesn't require the same level of monitoring, versioning, and data pipeline integration that would be needed for deploying a model in a larger, production level software application.