import numpy
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
params = [int(x) for x in input().split()]
Y_col = params[0]
#print(params)
H = []
predict = []
for i in range(0, params[1]):
    H.append([float(x) for x in input().split()])
#print(H[:2][:5])
X = [H[i][0:params[0]] for i in range(0,params[1])]
Y = [H[i][Y_col] for i in range(0,params[1])]

numPred = input()
#print(int(numPred))
for i in range(0, int(numPred)):
    predict.append([float(x) for x in input().split()])
poly = PolynomialFeatures(degree=params[0]+1)
X_ = poly.fit_transform(X)
predict_ = poly.fit_transform(predict)

clf = linear_model.LinearRegression(fit_intercept=False)
clf.fit(X_, Y)
for i in range(0,int(numPred)):
    print(clf.predict(predict_)[i])
