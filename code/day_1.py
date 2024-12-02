import pandas as pd
import os

input_name = "input_1.csv"
input_path = "inputs/" + input_name

input_data = pd.read_csv(os.path.abspath(input_path),
                         sep='\s+',
                         header=None)

list_1 = list(input_data[0])
list_2 = list(input_data[1])

list_1 = sorted(list_1)
list_2 = sorted(list_2)

distance = [None for x in list_1]
similarity_factor = [None for x in list_1]
similarity_score = [None for x in list_1]

for i in range(len(list_1)):
    distance[i] = abs(list_1[i] - list_2[i])
    similarity_factor[i] = list_2.count(list_1[i])
    similarity_score[i] = list_1[i] * similarity_factor[i]



print("The distance is ", sum(distance))
print("The similarity score is ", sum(similarity_score))
