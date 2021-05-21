import pandas as pd

# merge one_hot degree
degree = pd.read_csv('data/onehot_degreetype.csv')

cols = ['type_Bachelor', 'type_Master',
        'type_Other', 'type_OtherDiploma', 'type_PhD']
newcol = [','.join(i) for i in degree[cols].astype(str).values]
df = degree.assign(MergedDegree=newcol).drop(cols, 1)
df.to_csv('data/degree.csv')
# print(df)


# merge one_hot subject
subject = pd.read_csv('data/onehot_subject.csv')
cols = subject.columns.tolist()
cols = cols[3:]
newcol = [','.join(i) for i in subject[cols].astype(str).values]
df = subject.assign(MergedSubject=newcol).drop(cols, 1)
df.to_csv('data/subject.csv')
print(df)
