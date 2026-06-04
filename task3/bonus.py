import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

grayscale_image=np.random.randint(0,256,size=(200,300))
color_image=np.stack([grayscale_image,grayscale_image,grayscale_image],axis=2)

sepia_matrix = np.array([
    [0.393, 0.769, 0.189],
    [0.349, 0.686, 0.168],
    [0.272, 0.534, 0.131]
])
img_float=color_image.astype(np.float32)
h,w,c,=img_float.shape
pixels=img_float.reshape(-1,3)
sepia_pixels=pixels @ sepia_matrix.T
sepia_pixels=np.clip(sepia_pixels,0,255).astype(np.uint8)
sepia_image=sepia_pixels.reshape(h,w,c)

R=img_float[:,:,0]
G=img_float[:,:,1]
B=img_float[:,:,2]
L=0.299*R+0.587*G+0.114*B
alpha=1.5
R_new=L+alpha*(R-L)
G_new=L+alpha*(G-L)
B_new=L+alpha*(B-L)
saturated_image=np.stack([R_new,G_new,B_new],axis=2)
saturated_image=np.clip(saturated_image,0,255).astype(np.uint8)

border_width=20
result_float=img_float.copy()
coeff_left=np.linspace(0,1,border_width)
result_float[:,:border_width,:]=img_float[:,:border_width,:]*coeff_left.reshape(1,-1,1)
coeff_right=np.linspace(0,1,border_width)
right_start=w-border_width
result_float[:,right_start:,:]=img_float[:,right_start:,:]*(1-coeff_right.reshape(1,-1,1))+255*coeff_right.reshape(1,-1,1)
result_image=np.clip(result_float,0,255).astype(np.uint8)

plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.imshow(color_image)
plt.title('原始图像')
plt.subplot(2,2,2)
plt.imshow(sepia_image)
plt.title('复古色滤镜')
plt.subplot(2,2,3)
plt.imshow(saturated_image)
plt.title('过饱和效果')
plt.subplot(2,2,4)
plt.imshow(result_image)
plt.title('渐变边框')
plt.tight_layout()
plt.show()







