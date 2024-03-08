import pandas as pd
import random


PATH_IR = "mock_data/mock_ir.csv"
PATH_MIC = "mock_data/mock_mic.csv"

df_mic = pd.read_csv(PATH_MIC)
df_mic.set_index("time [s]", inplace= True)
df_mic = df_mic[0.2:0.5]

df_ir = pd.read_csv(PATH_IR)
df_ir.set_index("time [s]", inplace= True)
df_ir = df_ir[0.2:0.5]


def get_data_mock():
    key = "pos" if random.choice([True, False]) else "neg"
    filtered_strings = [s for s in df_ir.columns if s.startswith(key)]
    print(filtered_strings)
    id = random.choice(filtered_strings)
    new_data = pd.DataFrame({"IR":df_ir[id], "MIC":df_mic[id]})
    new_data["time"] = new_data.index
    return new_data.to_dict(orient='list'), True if key  == "pos" else False

if __name__ == "__main__":
    print(get_data_mock())

