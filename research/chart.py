import matplotlib.pyplot as plt

# data to plot 
labels = ["apples", "bananas", "cheries", "dates"]
sized = [30, 23, 20, 25]
colors =['red', 'yellow', 'pink', 'brown']
explode = (0.1, 0, 0, 0)


plt.pie(sized, labels=labels, colors=colors, explode=explode, autopct="%1.1f%%", startangle=140, shadow=True)
plt.title("Fruit Productoin")
plt.show()

