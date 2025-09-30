import pytest
import logging
import pandas as pd
import pandas.testing as pdt
from project_functions import long_lat, stand_value, remove_values_from_column, map_dtype, train_model, evaluate_model, build_basic_model
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization, Input
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from unittest.mock import patch

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])

# Mock data for testing
street_names = ['Backer en Ruebweg', 'Nieuwe Kadijk', 'Graaf Engelbertlaan', 'Ettensebaan', 'Tramsingel', 'Franklin Rooseveltlaan']
longitudes = [4.735870517806607, 4.805146141028703, 4.757699198974637, 4.732075503705787, 4.765561273223476, 4.810410549597804]
latitudes = [51.60179951753548, 51.60000819477735, 51.569853623757176, 51.58050315417642, 51.590071305296476, 51.57978725868066]

values_list_car = ["Car", "Delivery Van", "Moped", "Bicycle", "Light-moped", "Lorry", "Motorcylce", "Bus"]
standardized_list_car = [-0.350029334776985, 0.38036674264997405, 2.571554974930851, -1.810821489630903, 1.110762820076933, 1.8411588975038922, 3.30195105235781, -1.080425412203944]

df = pd.DataFrame({'Col_1': [1, 2, 3], 'Col_2': [4, 0, 5], 'Col_3': [6, 7, 8]})

df_dtype = pd.DataFrame({'Integer': [1, 2, 3], 'Float': [1.1, 2.4, 8.2], 'Boolean':[True, False, True], 'Timestamp':['2014-01-02', '2016-9-3', '2017-8-8'], 'Text':['Text_1', 'Text_2', 'Text_3']})
df_dtype['Timestamp'] = pd.to_datetime(df_dtype['Timestamp'])

@pytest.fixture
def mock_data():
    """
    Fixture providing mock data for model testing.

    Returns:
        tuple: X_train, y_train, X_val, y_val, X_test, y_test
    """
    X_train = np.random.rand(100, 20)
    y_train = np.random.randint(2, size=100)
    X_val = np.random.rand(20, 20)
    y_val = np.random.randint(2, size=20)
    X_test = np.random.rand(20, 20)
    y_test = np.random.randint(2, size=20)
    return X_train, y_train, X_val, y_val, X_test, y_test

def test_long_lat():
    """
    Test for long_lat function.
    """
    logging.info("Starting test_long_lat")

    assert long_lat('Nieuwe Kadijk', street_names, longitudes, latitudes) == (4.805146141028703, 51.60000819477735)
    assert long_lat('Backer en Ruebweg', street_names, longitudes, latitudes) == (4.735870517806607, 51.60179951753548)
    assert long_lat('Graaf Engelbertlaan', street_names, longitudes, latitudes) == (4.757699198974637, 51.569853623757176)
    assert long_lat('Ettensebaan', street_names, longitudes, latitudes) == (4.732075503705787, 51.58050315417642)
    assert long_lat('Tramsingel', street_names, longitudes, latitudes) == (4.765561273223476, 51.590071305296476)
    assert long_lat('Franklin Rooseveltlaan', street_names, longitudes, latitudes) == (4.810410549597804, 51.57978725868066)

    logging.info("Finished test_long_lat")

def test_stand_value():
    """
    Test for stand_value function.
    """
    logging.info("Starting test_stand_value")

    assert stand_value("Car", values_list_car, standardized_list_car) == -0.350029334776985
    assert stand_value("Delivery Van", values_list_car, standardized_list_car) == 0.38036674264997405
    assert stand_value("Moped", values_list_car, standardized_list_car) == 2.571554974930851
    assert stand_value("Bicycle", values_list_car, standardized_list_car) == -1.810821489630903
    assert stand_value("Light-moped", values_list_car, standardized_list_car) == 1.110762820076933
    assert stand_value("Lorry", values_list_car, standardized_list_car) == 1.8411588975038922
    assert stand_value("Motorcylce", values_list_car, standardized_list_car) == 3.30195105235781
    assert stand_value("Bus", values_list_car, standardized_list_car) == -1.080425412203944

    logging.info("Finished test_stand_value")

def test_remove_values_from_column():
    """
    Test for remove_values_from_column function.
    """
    logging.info("Starting test_remove_values_from_column")

    pdt.assert_frame_equal(remove_values_from_column(df, 'Col_2', [0, 1, 2]).reset_index(drop=True), df[~df['Col_2'].isin([0, 1, 2])].reset_index(drop=True))
    pdt.assert_frame_equal(remove_values_from_column(df, 'Col_1', [0, 1, 2]).reset_index(drop=True), df[~df['Col_1'].isin([0, 1, 2])].reset_index(drop=True))
    pdt.assert_frame_equal(remove_values_from_column(df, 'Col_3', [6, 1, 2]).reset_index(drop=True), df[~df['Col_3'].isin([6, 1, 2])].reset_index(drop=True))

    logging.info("Finished test_remove_values_from_column")

def test_map_dtype():
    """
    Test for map_dtype function.
    """
    logging.info("Starting test_map_dtype")

    assert map_dtype(df_dtype['Integer'].dtype) == 'INTEGER'
    assert map_dtype(df_dtype['Float'].dtype) == 'REAL'
    assert map_dtype(df_dtype['Boolean'].dtype) == 'BOOLEAN'
    assert map_dtype(df_dtype['Timestamp'].dtype) == 'TIMESTAMP'
    assert map_dtype(df_dtype['Text'].dtype) == 'TEXT'

    logging.info("Finished test_map_dtype")

def test_build_basic_model():
    """
    Test for build_basic_model function.
    """
    logging.info("Starting test_build_basic_model")

    input_shape = (20,)
    model = build_basic_model(input_shape)
    assert isinstance(model, Sequential), "Model is not a Keras Sequential model"
    assert len(model.layers) == 7, "Model does not have the correct number of layers"

    logging.info("Finished test_build_basic_model")

def test_train_model(mock_data):
    """
    Test for train_model function.
    """
    logging.info("Starting test_train_model")

    X_train, y_train, X_val, y_val, _, _ = mock_data
    model = build_basic_model((20,))
    history = train_model(model, X_train, y_train, X_val, y_val)
    assert 'accuracy' in history.history, "Training history does not contain 'accuracy'"
    assert 'val_accuracy' in history.history, "Training history does not contain 'val_accuracy'"

    logging.info("Finished test_train_model")

@patch('model_module.print')
def test_evaluate_model(mock_print, mock_data):
    """
    Test for evaluate_model function.
    """
    logging.info("Starting test_evaluate_model")

    _, _, _, _, X_test, y_test = mock_data
    model = build_basic_model((20,))
    model.fit(X_test, y_test, epochs=1)  # Fit briefly to initialize the model
    evaluate_model(model, X_test, y_test)
    
    # Ensure print was called at least once
    assert mock_print.called, "Print function was not called"

    logging.info("Finished test_evaluate_model")

if __name__ == "__main__":
    logging.info("Starting pytest")

    result = pytest.main(["-v", __file__])

    logging.info(f'Pytest finished with result code: {result}')
