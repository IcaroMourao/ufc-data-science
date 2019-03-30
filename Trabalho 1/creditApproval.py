#-*- coding: utf-8 -*-

import numpy as np
import math
from random import randint
from matplotlib import pyplot as plt
#np.set_printoptions(threshold=np.inf)

X = np.genfromtxt(fname='crx.data',
					delimiter=',',
					dtype=np.float32)

def buildSet():

	X_train = X
	X_train = np.delete(X_train, 15, axis=1)

	a = np.array([1,0])
	b = np.array([0,1])
	Y1 = np.tile(a,(307,1))
	Y2 = np.tile(b,(383,1))

	Y_train = np.concatenate((Y1,Y2),0)

	X_test = X_train
	Y_test = Y_train
	test_index = []
	train_index = []

	while len(test_index) < 138:
		n_rand = randint(0, 689)
		if n_rand not in test_index:
			test_index.append(n_rand)
	
	test_index = sorted(test_index, reverse=True)

	for i in range(0,690):
		if i not in test_index:
			train_index.append(i)

	train_index = sorted(train_index, reverse=True)

	for i in test_index:
		X_train = np.delete(X_train, i, axis=0)
		Y_train = np.delete(Y_train, i, axis=0)

	for i in train_index:
		X_test = np.delete(X_test, i, axis=0)
		Y_test = np.delete(Y_test, i, axis=0)

	return (X_train.T, X_test.T, Y_train.T, Y_test)

def classifier(X_train, X_test,Y_train,Y_test):
	A = Y_train.dot(X_train.T).dot(np.linalg.pinv(X_train.dot(X_train.T)))

	Y_result = A.dot(X_test)
	Y_result = Y_result.T

	successP = 0
	successM = 0

	for i in range(0, len(Y_result)):
		comp = Y_result[i]
		if comp[0] > comp[1]:
			if False not in (Y_test[i] == [1,0]):
				successP += 1
		else:
			if False not in (Y_test[i] == [0,1]):
				successM += 1
	
	return (successP, successM)

def main():
	result = []
	class1 = []
	class2 = []
	test = []

	for i in range(0,100):
		t = buildSet()
		c = classifier(t[0],t[1],t[2],t[3])
		result.append(round((((c[0]+c[1])/138)*100), 2))
		class1.append(round((c[0]/138)*100,2))
		class2.append(round((c[1]/138)*100,2))
		test.append(i+1)

	print(result)
	print('Mean: {}%'.format(round(np.mean(result),2)))
	print('Max: {}%'.format(np.max(result)))
	print('Min: {}%'.format(np.min(result)))
	print('Standard deviation: {}'.format(np.std(result)))
	print('Mean of class +: {}%'.format(round(np.mean(class1),2)))
	print('Mean of class -: {}%'.format(round(np.mean(class2),2)))

	plt.plot(test, result, color='black', marker='.', linestyle='solid')
	plt.title('Success in percentage for each test')
	plt.ylabel('Success Pecentage')
	plt.xlabel('Test')
	plt.show()

if __name__ == "__main__":
    main()