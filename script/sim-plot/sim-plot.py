from typing import List
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd
import subprocess
from subprocess import PIPE
import io
    

def cut_data(raw : str) -> str:
    print(raw)
    first_split = raw.split('.END')
    if len(first_split) > 1:
        second_split = first_split[len(first_split)-1].split('loop count')
        if len(second_split) >1:
            return second_split[0]
        else:
            print("ERROR1")
            sys.exit
    else:
        print("ファイルの最後に「.end」が見つかりません。")
        sys.exit

def simulation(filepath : str) -> pd.DataFrame:
    result = subprocess.run(["pjsim_n", filepath], stdout=PIPE, stderr=PIPE, text=True)
    data = cut_data(result.stdout)
    df = pd.read_table(io.StringIO(data),index_col=0,header=None,sep=' ')
    df.drop(len(df.columns) ,axis=1, inplace=True)
    return df


if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
        if os.path.exists(filepath):
            simulation(filepath)
            df = simulation(filepath)
            print(df)
            df.plot()
            plt.show()
        else:
            print("ファイルが存在しません。\n指定されたパス:"+filepath)
    else:
        print("引数が足りません。\n入力された引数:"+str(len(sys.argv)))