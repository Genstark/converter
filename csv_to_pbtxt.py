import pandas

file = pandas.read_csv("dataset/train_labels.csv")
print(file)

specific_column=file["class"]
print("The column is:")
print(specific_column)

classes = []

for i in specific_column:
    if i not in classes:
        classes.append(i)
        classes.sort()

with open("dataset/class-name.txt", "w") as f:
    for i in classes:
        f.write("{}\n".format(i))