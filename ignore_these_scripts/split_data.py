import duckdb
import pandas as pd

iris_pdf = pd.read_csv("/workspace/data/iris_dataset.csv")

print(iris_pdf.head())

pdf_part_1 = iris_pdf.iloc[:, [0, 1, 2, 4]]
pdf_part_2 = iris_pdf.iloc[:, [0, 2, 3, 4]]

print(pdf_part_1.head())
print(pdf_part_2.head())

pdf_part_1.to_csv("/workspace/data/iris_dataset_part_1.csv", index=False)
pdf_part_2.to_csv("/workspace/data/iris_dataset_part_2.csv", index=False)
