import matplotlib.pyplot as plt
x=[2,10,20,50]  #number of candidate classes
y=[21,38,39.5,42] #accuracies achieved
plt.plot(x,y,label='')
plt.xlabel('number of candidate classes')
plt.ylabel('accuracy')
plt.title('number of candidate classes vs accuracies')
plt.show()
