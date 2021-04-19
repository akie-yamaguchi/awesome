#Matplotlib

import matplotlib.pyplot as plt 
import numpy as np

%matplotlib inline

x = np.arange(10)
y = np.random.randint(-10, 10, 10)

plt.plot(x, y)#折れ線
plt.annotate('max value', xy =(4.2, 0), xytext =(9, 1),arrowprops = dict(facecolor= 'red', shrink = 0.05))

x1 = np.random.randint(10, 20 ,20)
x2 = np.random.randint(20, 30, 20)
y1 = np.random.randint(50, 100, 20)
y2 = np.random.randint(0, 40, 20)

plt.scatter(x1,x2, marker ='*')#散布図
plt.scatter(y1,y2, marker = '+')

data = np.random.randint(0, 10, 10)
plt.hist(data, bins =15) #細かく指定 ヒストグラム

x =['sunny' ,'cloudy', 'rainy', 'windy']
y = np.random.randint(0, 200, 4)
plt.bar(x, y) #棒グラフ

x =np.arange(10)
y = np.random.randint(-10, 10, 10)
plt.plot(x, y)
plt.title('Result') #タイトル
plt.xlabel('x axis')　#ラベル
plt.ylabel('y axis')　#ラベル

x1 = np.random.randint(10, 20, 20)
x2 =np.random.randint(20, 30, 20)
y1 = np.random.randint(50, 100, 20)
y2 = np.random.randint(0, 40, 20)

plt.scatter(x1, x2)
plt.scatter(y1, y2)
plt.xlim(0, 40)
plt.ylim(0, 120)

x = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(x) 
y2 = np.cos(x)

plt.plot(x, y1, label ='sin')
plt.plot(x, y2, label ='cos')

plt.ylim(-2, 2)
plt.legend(loc=2) #左上に表示