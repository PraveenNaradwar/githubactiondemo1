import pandas as pd

print("Extract data from Mysql database")

data={
    "id":[101,102,103],
    "name":['sanjay','priyanka','komal'],
    "age":[25,26,27]
}

df=pd.DataFrame(data)
print(df)