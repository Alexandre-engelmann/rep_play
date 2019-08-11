import numpy as np
my_list = [1,2,3]
x=np.array(my_list)
my_matrix = [[1,2,3,],[4,5,6],[7,8,9]]
np.array(my_matrix)
list(range(0,5))
np.arange(0,5)
np.arange(0,11,2)
#working Viviane
np.arange(1,100,3)
np.arange(100,1,-3)
#end working Viviane
np.zeros(3)
np.zeros(3,5) #numbers of rows and number of columns
np.ones(4)
np.ones((3,3))
np.linspace(0,10,30)
np.linspace(0,10,51)
np.eye(4)
#random number arrays
np.random.rand(1)
np.random.rand(5,5)
np.random.randn(5)#center of 0 and variance 1
np.random.randint(1,100)
np.random.randint(1,100,10)
arr=np.arange(25)
ranarr=np.random.randint(0,50,10)
arr.reshape(5,5)
arr.shape
arr.reshape(5,5).shape
arr.reshape(25,1).shape
arr.dtype
ranarr.max()
ranarr.argmax()
ranarr.argmin()
