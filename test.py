import pandas as pd

data=[
    {"name":"Hans","age":23,"city":"New Delhi"},
    {"name":"Mohit","age":23,"city":"New Delhi"},
    {"name":"Yash","age":23,"city":"New Delhi"},
    {"name":"Vikash","age":28,"city":"New Delhi"}
]

df = pd.DataFrame(data)

df.to_csv("data/data.csv", index=False)