# General regression model for two independent variables
import pandas
from sklearn import linear_model
from sklearn.metrics import r2_score

# take input from the user in the form of comma seperated values and store it in a list do this for x and y
x1 = list(map(int, input("Enter the values of x1: ").split(",")))
x2 = list(map(int, input("Enter the values of x2: ").split(",")))
y = list(map(int, input("Enter the values of y: ").split(",")))

# create a dataframe using pandas
df = pandas.DataFrame({'X1': x1, 'X2': x2, 'Y': y})

X = df[['X1', 'X2']]
y = df['Y']
regr = linear_model.LinearRegression()
regr.fit(X.values, y)

y_pred = []
y_obs = []
for ind in X.index:
    y_pred.append(regr.predict([[X['X1'][ind],X['X2'][ind]]])[0])
    y_obs.append(y[ind])

print("Output for linear method")
print("r^2 = " , r2_score(y_obs,y_pred))
print('y =' , regr.intercept_  , '+',  regr.coef_[0]  , 'X1 +' , regr.coef_[1] , 'X2')

x_sqr_val = []
for ind in X.index:
    x_sqr_val.append([X['X1'][ind] , X['X2'][ind] , (X['X1'][ind])^2 , (X['X2'][ind])^2])

quad_regr = linear_model.LinearRegression()
quad_regr.fit(x_sqr_val,y_obs)

y_pred = []
y_obs = []
for ind in X.index:
    y_pred.append(quad_regr.predict([[X['X1'][ind] , X['X2'][ind] ,(X['X1'][ind])^2 , (X['X2'][ind])^2]])[0])
    y_obs.append(y[ind])

print("Output for quadratic method")
print("r^2 = " , r2_score(y_obs,y_pred))
print('y =' , quad_regr.intercept_  , '+',  quad_regr.coef_[0]  , 'X1 +' , quad_regr.coef_[1] , 'X2' , '+',  quad_regr.coef_[2]  , 'X1^2 +' , quad_regr.coef_[3] , 'X2^2' )