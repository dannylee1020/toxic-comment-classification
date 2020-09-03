import numpy as np
from keras.models import load_model

import config

def test_model_prediction():
	# Given 
	test = np.load(open(config.LOCAL_FILE_DIR + config.TEST_DATA, 'rb'))
	test_short = test[:30]

	# When
	model = load_model(config.LOCAL_FILE_DIR + config.MODEL)
	y_pred = model.predict(test_short)

	# Then
	assert y_pred is not None
	assert len(y_pred) == len(test_short)
	assert y_pred.shape == (len(test_short), 6)