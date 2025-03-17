# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle


loaded_model= pickle.load(open('E:/Parkin/trained_model.sav','rb'))
#evaluting by input


input_data=(117.226	,123.925,	106.656,	0.00417,	0.00004,	0.00186,	0.0027,	0.00558,	0.01909,	0.171,	0.00864,	0.01223,	0.01949,	0.02592,	0.00955,	23.079,	0.603515,	0.669565,	-5.61907,	0.191576,	2.027228,	0.215724)
#convert tuple into numpy array
input_data_as_numpy_array=np.asarray(input_data)
#reshape the array because eta na hole model main dataset er row column ke dhore boshe thakbe. tai 1 ta data point er jonno reshape kora lage

input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

#difference is here at loaded_model keyword here we store all value of traning
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if prediction[0]==0:
  print('Healthy')
else:
  print('Parkinsons affected')