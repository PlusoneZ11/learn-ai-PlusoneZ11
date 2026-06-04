import numpy as np

data_matrix=np.arange(100).reshape(10,10)
print("原矩阵：\n")
print(data_matrix)

center=data_matrix[3:7,3:7]
print("\n中心的4×4子矩阵：")
print(center)

mask=data_matrix>75
data_matrix[mask]=0
print("\n将>75的元素置零：")
print(data_matrix)

data_matrix=data_matrix.astype(np.float64)
data_matrix*=0.8
print("\n乘以0.8：")
print(data_matrix)

max_val=np.max(data_matrix)
print(f"\n最终矩阵的最大值：{max_val}")

f_idx=np.argmax(data_matrix)
r_idx, c_idx = np.unravel_index(f_idx, data_matrix.shape)
print(f"最大值所在的行索引：{r_idx}，列索引：{c_idx}")


























