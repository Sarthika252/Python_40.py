import matplotlib.pyplot as plt
x=[1,2,3,12,2,4,4]
y=[3,2,1,4,5,6,7]
plt.bar(x,y)
plt.barh(x,y)
plt.title("Bar Chart")
plt.legend(["bar"])
plt.show()