Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv(r"C:\Users\user\Downloads\Nairobi Office Price Ex.csv")
data = dataset[['SIZE', 'PRICE']]

def MeanSquaredError(m,b,points)
SyntaxError: expected ':'
def MeanSquaredError(m, b, points):
    total_error=0
    for i in range(len(points)):
        x=points.iloc[i].SIZE
        y=points.iloc[i].PRICE
        total_error +=(y-(m*x+b))**2
    return total_error/float(len(points))

def gradient_descent(m_now, b_now, points, learning_rate):
    m_gradient=0
    b_gradient=0
    n=len(points)
    for i in range(n):
        x = points.iloc[i].SIZE
        y = points.iloc[i].PRICE
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
     m= m_now - m_gradient * learning_rate
     
SyntaxError: unindent does not match any outer indentation level
def gradient_descent(m_now, b_now, points, learning_rate):
    m_gradient = 0
    b_gradient = 0
    n = len(points)
    for i in range(n):
        x = points.iloc[i].SIZE
        y = points.iloc[i].PRICE
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    m = m_now - m_gradient * learning_rate
    b = b_now - b_gradient * learning_rate
    return m, b

m=0
b=0
learning_rate=0.0001
epochs=10
error=[]
for epoch in range(epochs):
    m, b = gradient_descent(m, b, data, learning_rate)
    error = MeanSquaredError(m, b, data)
    errors.append(error)
    print(f"Epoch {epoch+1}: Mean Squared Error = {error}")

Traceback (most recent call last):
  File "<pyshell#44>", line 4, in <module>
    errors.append(error)
NameError: name 'errors' is not defined. Did you mean: 'error'?
>>> errors=[]
>>> for epoch in range(epochs):
...     m, b = gradient_descent(m, b, data, learning_rate)
...     error = MeanSquaredError(m, b, data)
...     errors.append(error)
...     print(f"Epoch {epoch+1}: Mean Squared Error = {error}")
... 
Epoch 1: Mean Squared Error = 334.35761896621045
Epoch 2: Mean Squared Error = 135.211659230609
Epoch 3: Mean Squared Error = 88.99986991322581
Epoch 4: Mean Squared Error = 78.27643111370033
Epoch 5: Mean Squared Error = 75.788058545839
Epoch 6: Mean Squared Error = 75.21063181936948
Epoch 7: Mean Squared Error = 75.07663977891475
Epoch 8: Mean Squared Error = 75.04554668855342
Epoch 9: Mean Squared Error = 75.03833128359885
Epoch 10: Mean Squared Error = 75.03665669184075
>>> plt.scatter(data['SIZE'], data['PRICE'], color='blue', label='Data Points')
<matplotlib.collections.PathCollection object at 0x00000174FF0AC830>
>>> predicted_prices = m * data['SIZE'] + b
>>> plt.plot(data['SIZE'], predicted_prices, color='red', label='Line of Best Fit')
[<matplotlib.lines.Line2D object at 0x00000174FF5E35F0>]
>>> plt.xlabel("Office Size (sq. ft)")
Text(0.5, 0, 'Office Size (sq. ft)')
>>> plt.ylabel("Office Price")
Text(0, 0.5, 'Office Price')
>>> plt.legend()
<matplotlib.legend.Legend object at 0x00000174FF5E37A0>
>>> plt.title("Office Size vs Price with Line of Best Fit")
Text(0.5, 1.0, 'Office Size vs Price with Line of Best Fit')
>>> 
>>> plt.show()
>>> price100sq=m * 100 + b
>>> price100sq
136.27943991466574
