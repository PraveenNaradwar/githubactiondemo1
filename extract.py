import pandas as pd

print("Extract data from Mysql database")

data={
    "id":[101,102,103,104],
    "name":['sanjay','priyanka','komal','priti'],
    "age":[25,26,27,28]
}

df=pd.DataFrame(data)
print(df)