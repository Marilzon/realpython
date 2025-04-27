import pandas as pd
import json

input_data = "real_cases/json_normalize/data/data.json"
output_data = "real_cases/json_normalize/data/output.json"

with open(input_data, 'r') as f:
    data = json.load(f)

df = pd.json_normalize(data)

df.to_json(output_data)

print(df)
