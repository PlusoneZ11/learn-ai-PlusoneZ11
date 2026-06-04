import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False

def logistic(x,L=1,k=1,x0=0):
    return L/(1+np.exp(-k*(x-x0)))
x=np.linspace(-8,8,500)
fig,axes=plt.subplots(2,2,figsize=(12,10))
fig.suptitle('Logistic函数及其参数影响分析', fontsize=16, fontweight='bold')

ax1=axes[0,0]
L,k,x0=1,1,0
y=logistic(x,L,k,x0)
ax1.plot(x,y,linewidth=2,label=f'标准函数: L={L}, k={k}, x0={x0}')
ax1.set_title("Logistic函数")
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.axhline(L,color='r',linestyle='--',alpha=0.5,linewidth=1,label=f'饱和值 L={L}')
ax1.axvline(x0,color='g',linestyle='--',alpha=0.5,linewidth=1,label=f'中点 x0={x0}')
ax1.grid(True,alpha=0.5)
ax1.legend()
ax1.set_ylim(-0.1,1.2)


ax2=axes[0,1]
k,x0=1,0
L_values=[0.5,1,1.5,2]
colors=['orange', 'purple', 'red', 'blue']
for L_v,col in zip(L_values,colors):
    y=logistic(x,L=L_v,k=k,x0=x0)
    ax2.plot(x,y,color=col,linewidth=2,label=f'L={L_v}')
ax2.set_title('不同L值对曲线的影响\n控制函数的最大值')
ax2.set_xlabel("x")
ax2.set_ylabel("f(x)")
ax2.grid(True,alpha=0.3)
ax2.legend()
ax2.set_ylim(-0.1,2.2)


ax3=axes[1,0]
L,x0=1,0
k_values=[0.3,0.8,1.5,3]
for k_v,col in zip(k_values,colors):
    y=logistic(x,L=L,k=k_v,x0=x0)
    ax3.plot(x,y,color=col,linewidth=2,label=f'k={k_v}')
ax3.set_title('不同k值对曲线的影响\n控制曲线的陡峭程度')
ax3.set_xlabel("x")
ax3.set_ylabel("f(x)")
ax3.grid(True,alpha=0.3)
ax3.legend()

ax4=axes[1,1]
L,k=1,1
x0_values=[-3,0,2,4]
for x0_v,col in zip(x0_values,colors):
    y=logistic(x,L=L,k=k,x0=x0_v)
    ax4.plot(x,y,color=col,linewidth=2,label=f'x0={x0_v}')
ax4.set_title('不同x0值对曲线的影响\n控制曲线在x轴上的平移')
ax4.set_xlabel("x")
ax4.set_ylabel("f(x)")
ax4.grid(True,alpha=0.3)
ax4.legend()

plt.tight_layout()
plt.show()
plt.figure(figsize=(14,5))













