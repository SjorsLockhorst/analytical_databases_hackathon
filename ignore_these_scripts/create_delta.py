import pandas as pd

from deltalake import write_deltalake

df = pd.read_csv("/workspace/data/iris_dataset_part_1.csv")
write_deltalake("/workspace/data/iris_dataset_part_1", df)
