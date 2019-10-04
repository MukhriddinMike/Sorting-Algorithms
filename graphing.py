import matplotlib.pyplot as plt


Number = [10, 100, 1000,10000, 100000, 1000000]
Bubble_sort = [0.0030148, 0.000999, 0.00599, 0.00799, 0.05898, 0.5446]
Selection_sort = [0.000999, 0.00199, 0.266, 21.692, 220.999,2340.455]
Insertion_sort = [0.0009992, 0.001, 0.00399, 0.00599, 0.0659, 0.78255]
plt.plot(Number, Insertion_sort, color='g')
#plt.plot(Number, Selection_sort, color='orange')
plt.plot(Number, Bubble_sort, color='c')
plt.xlabel('Time')
plt.ylabel('Number')
plt.title('Best Case Bubble sort/ Insertion sort')
plt.show()
