import os
import dill

import numpy as np

#Global variables for filepath for this example
#In production would have reusable functions to take model name and grab from storage

MODEL_FILEPATH = "test_model.pkl"
ABSOLUTE_MODEL_PATH = os.path.abspath(MODEL_FILEPATH)

ENCODER_FILEPATH = "label_encoder.pkl"
ABSOLUTE_ENCODER_PATH = os.path.abspath(ENCODER_FILEPATH)

def load_serialized_object(filepath:os.PathLike):
    with open(filepath, "rb") as f:
        return dill.load(f)

def make_prediction(wine_features:list):

    #Format feature vector for input to model
    input_features = np.array(wine_features).reshape(1,-1)

    model = load_serialized_object(ABSOLUTE_MODEL_PATH)

    encoder = load_serialized_object(ABSOLUTE_ENCODER_PATH)

    prediction = model.predict(input_features)

    wine_quality = encoder.inverse_transform(prediction)[0]

    return str(wine_quality)