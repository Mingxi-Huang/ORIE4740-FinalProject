import pandas as pd

degree = pd.read_csv('data/degree.csv')
print("Degree shape")
print(degree.shape)
subject = pd.read_csv('data/subject.csv')
print("Subject shape")
print(subject.shape)
total_funds = pd.read_csv('data/sum_usa_funds.csv')
print("Total_funds shape")
print(total_funds.shape)

with_degree = total_funds.merge(
    degree, left_on='object_id', right_on='object_id')
print(with_degree.head(10))
# TODO: connect p:xxx and c:xxx through relationship.csv
