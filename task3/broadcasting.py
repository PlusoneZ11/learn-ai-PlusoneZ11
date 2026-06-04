import numpy as np

points_A=np.random.randint(101,size=(5, 2))
points_B=np.random.randint(101,size=(8, 2))

dif=points_A[:,np.newaxis,:]-points_B[np.newaxis,:,:]
distance_matrix=np.sqrt(np.sum(dif**2,axis=2))
print(distance_matrix)

min_distance=np.min(distance_matrix,axis=1)
print(min_distance)

mask_close=distance_matrix<20
idx=np.where(np.any(mask_close,axis=0))[0]
print(idx)