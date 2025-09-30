import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, Input
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

def stand_value(value, values_list, standardized_list):
    """
    This function takes a string value, a values list and a list with standardized values. The function returns the standardized number correlating to the value input.
    
    Parameters:
    -----------
    - value: The value you want the standardized number for.
    - values_list: The list of all possible values.
    - standardized_list: The list of all standardized number correlating to each possible value.

    Returns:
    --------
    - new_value: The standardized number correlating with the passed value.
    """
    
    new_value = 0
    for i in range(0, len(values_list)):
        if values_list[i] == value:
            new_value = standardized_list[i]
    
    return new_value

def long_lat(street, street_names, longitudes, latitudes):
    """
    This function takes a street name passed as a string, a list of all available street names, a list of all avaliable longitudes and a list of all available latitudes and returns the longitude and latitude matching the street.

    Parameters:
    -----------
    - street: The street name the longitude and latitudes are needed for.
    - street_names: The list of all available street names.
    - longitudes: The list of all available longitudes.
    - latitudes: The list of all available longitudes.

    Returns:
    --------
    - long: The longitude needed.
    - lat: The latitude needed.
    """

    long = 0
    lat = 0
    for i in range(0, len(street_names)):
        if street_names[i] == street:
            long = longitudes[i]
            lat = latitudes[i]
    
    return long, lat

def remove_values_from_column(df, column, values):
    """
    Removes rows from the DataFrame based on specified values from column.
    
    Parameters:
    -----------
    df (pd.DataFrame): The DataFrame to be filtered.
    column (string): The name of to column to be filtered by.
    values (list): A list of values to be removed.
    
    Returns:
    --------
    pd.DataFrame: The filtered DataFrame.
    """

    for value in values:
        df = df[df[column] != value]
    return df

def map_dtype(dtype):
    """
    This function takes as input a pandas data type and returns a PostgreSQL data type
    
    Parameters:
    -----------
    dtype: The pandas data type
    
    Returns:
    --------
    The mathcing PostgreSQL data type
    """

    if pd.api.types.is_integer_dtype(dtype):
        return 'INTEGER'
    elif pd.api.types.is_float_dtype(dtype):
        return 'REAL'
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'TIMESTAMP'
    else:
        return 'TEXT'

# Function to train the model with early stopping and model checkpoint
def train_model(model, X_train, y_train, X_val, y_val):
    """
    Trains a neural network model on the provided training data and evaluates it on validation data.

    Parameters:
    -----------
    model : keras.Model
        The neural network model to be trained.
    X_train : numpy.ndarray
        The training data features.
    y_train : numpy.ndarray
        The training data labels.
    X_val : numpy.ndarray
        The validation data features.
    y_val : numpy.ndarray
        The validation data labels.

    Returns:
    --------
    history : keras.callbacks.History
        A History object containing the training history, including loss and metrics values,
        for each epoch.
    """
    early_stopping = EarlyStopping(patience=10, restore_best_weights=True)
    model_checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True)
    reduce_lr = ReduceLROnPlateau(patience=5, factor=0.5, min_lr=0.00001)

    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=100,
        batch_size=32,
        callbacks=[early_stopping, model_checkpoint, reduce_lr]
    )

    return history

def evaluate_model(model, X_test, y_test):
    """
    Evaluates a trained classification model on the provided test data.

    Parameters:
    -----------
    model : keras.Model
        The trained classification model.
    X_test : numpy.ndarray
        Test data features.
    y_test : numpy.ndarray
        Test data labels.

    Returns:
    --------
    None
        Prints evaluation metrics such as accuracy, precision, recall, F1 score,
        confusion matrix, and classification report.
    """

    y_pred = (model.predict(X_test) > 0.5).astype("int32")

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

def build_basic_model(input_shape):
    """
    Builds and compiles a basic feedforward neural network model for binary classification.

    Parameters:
    -----------
    input_shape : tuple
        Shape of the input data (excluding batch dimension).

    Returns:
    --------
    keras.Model
        Compiled Keras model for binary classification with the specified architecture:
        - Input layer matching input_shape
        - Dense layer with 64 units and 'relu' activation
        - Batch normalization layer
        - Dropout layer with dropout rate of 0.5
        - Dense layer with 32 units and 'relu' activation
        - Batch normalization layer
        - Dropout layer with dropout rate of 0.5
        - Output layer with 1 unit and 'sigmoid' activation
    """
    model = Sequential([
        Input(shape=input_shape),
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(32, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    return model