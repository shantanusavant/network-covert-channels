import pandas as pd
from sklearn import svm

# Importing dataset

test_raw = pd.read_csv("dataset_final.csv")
print(test_raw.head())
# Manipulating the dataset

test_raw['Identification'] = test_raw['Identification'].astype('category')
test_raw['Identification'] = test_raw['Identification'].cat.codes

test_raw['Source'] = test_raw['Source'].astype('category')
test_raw['Source'] = test_raw['Source'].cat.codes

test_raw['Destination'] = test_raw['Destination'].astype('category')
test_raw['Destination'] = test_raw['Destination'].cat.codes

test_raw['Protocol'] = test_raw['Protocol'].astype('category')
test_raw['Protocol'] = test_raw['Protocol'].cat.codes

test_raw['IP Flags'] = test_raw['IP Flags'].astype('category')
test_raw['IP Flags'] = test_raw['IP Flags'].cat.codes

test_raw['IP Header checksum'] = test_raw['IP Header checksum'].astype('category')
test_raw['IP Header checksum'] = test_raw['IP Header checksum'].cat.codes

test_raw['TCP Flags'] = test_raw['TCP Flags'].astype('category')
test_raw['TCP Flags'] = test_raw['TCP Flags'].cat.codes

test_raw['Info'] = test_raw['Info'].astype('category')
test_raw['Info'] = test_raw['Info'].cat.codes

test_raw['TCP Checksum'] = test_raw['TCP Checksum'].astype('category')
test_raw['TCP Checksum'] = test_raw['TCP Checksum'].cat.codes

# Dividing the dataset
test_raw = test_raw.sample(frac=1)
test_training = test_raw.iloc[0:int(test_raw.shape[0]/2), ]
test_test = test_raw.iloc[int(test_raw.shape[0]/2):, ]

print(test_raw.shape[0])
print("Training: ", test_training.shape[0])
print("Test: ", test_test.shape[0])

features_train = test_training[['Identification','Length','Source', 'Destination', 'IP Header checksum', 'IP Flags',  'TCP Flags']]
y_train = test_training["Value"].tolist()
features_test = test_test[['Identification','Length','Source', 'Destination', 'IP Header checksum', 'IP Flags', 'TCP Flags']]
y_true_test = test_test["Value"].tolist()
y_true_training = y_train

# training and predicting the accuracy

SVMModel = svm.SVC(kernel="linear") 
SVMModel.fit(features_train, y_train)

y_predict_test = SVMModel.predict(features_test)

y_predict_training = SVMModel.predict(features_train)

l = 100*sum(y_true_training == y_predict_training)/len(y_predict_training)
k = 100*sum(y_true_test == y_predict_test)*1.00/len(y_predict_test)*1.00

print("Linear Kernel, no regularization:")
print("Training Accuracy: ", l , "%")
print("Test Accuracy: ", k , "%")
