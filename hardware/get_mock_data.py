import pandas as pd
import random
from time import sleep

PATH_IR = "mock_data/mock_ir.csv"
PATH_MIC = "mock_data/mock_mic.csv"

df_mic = pd.read_csv(PATH_MIC)
df_mic.set_index("time [s]", inplace= True)
df_mic = df_mic[0.2:0.5]

df_ir = pd.read_csv(PATH_IR)
df_ir.set_index("time [s]", inplace= True)
df_ir = df_ir[0.2:0.5]


def command_daq(daq_arguments:dict):   
    items = ["neg_0", "pos_1", "pos_2", "neg_3", "pos_4"]
    id =  random.choice(items)    
    new_data = pd.DataFrame({"IR":df_ir[id], "MIC":df_mic[id]})
    new_data["time"] = new_data.index
    sleep(daq_arguments["duration"])
    return new_data.to_dict(orient='list')

if __name__ == "__main__":
    print(df_ir)
    # print(command_daq())

