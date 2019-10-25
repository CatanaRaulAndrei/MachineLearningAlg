import numpy as np
import matplotlib.pyplot as plt
# Least squares line
# m = (n * sum(xy)- sum(x)*sum(y)) / (n*sum(x*x) - sum(x)*sum(x))
# b = (sum(y) - m*sum(x))/n
# y = m*x + b
x = np.array([0, 2, 4, 6, 8 ,10, 12])
y = np.array([-0.8, -1, -0.2, 0.2, -0.2, 0.8, -0.6])
n = len(x)
sumxy = sum(np.multiply(x, y))
sumx = sum(x)
sumy = sum(y)
sumxx = sum(np.multiply(x, x))
# for m
numerator_m = n *sumxy - sumx*sumy
denominator_m = n*sumxx - sumx*sumx
m = numerator_m/denominator_m
# for b
b = (sumy - m*sumx)/n
# Linear Regression
print("Regression line: y = ",round(m,3),"*x",round(b,3))
# Plot LinearRegression
plt.scatter(x, y, color = "blue", marker = "o", s = 30)
y_pred = b + m * x
plt.plot(x, y_pred, color = "red")
plt.xlabel('x')
plt.ylabel('y')
plt.show()


