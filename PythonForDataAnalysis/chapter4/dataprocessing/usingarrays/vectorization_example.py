"""
vectorization: array expressions (faster than loops)
"""

import numpy as np
import matplotlib.pyplot as plt

points=np.arange(-5,5,0.01) # 1000 equally spaced pts
# # np.meshgrid: returns grid coords
# # xs,ys : (1000,1000), ranging
# # from -5 to 5, by 0.01 increments
# # : xs -5-to-5 range on row
# # : ys -5-to-5 range on col
xs,ys=np.meshgrid(points,points)

xs # xs.shape == (1000,1000)
# array([
#     [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
#     [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
#     [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
#     ...,
#     [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
#     [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
#     [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99]
# ])

ys # ys.shape == (1000, 1000)
# array([
#     [-5.  , -5.  , -5.  , ..., -5.  , -5.  , -5.  ],
#     [-4.99, -4.99, -4.99, ..., -4.99, -4.99, -4.99],
#     [-4.98, -4.98, -4.98, ..., -4.98, -4.98, -4.98],
#     ...,
#     [ 4.97,  4.97,  4.97, ...,  4.97,  4.97,  4.97],
#     [ 4.98,  4.98,  4.98, ...,  4.98,  4.98,  4.98],
#     [ 4.99,  4.99,  4.99, ...,  4.99,  4.99,  4.99]
# ])

# # square root on array sum of xs**2,ys**2
z=np.sqrt(xs**2 + ys**2)
# # still (1000,1000); sqrt of summed elements
# array([
#     [ 7.07106781,  7.06400028,  7.05693985, ...,
#       7.04988652, 7.05693985,  7.06400028],
#     [ 7.06400028,  7.05692568,  7.04985815, ...,
#       7.04279774, 7.04985815,  7.05692568],
#     [ 7.05693985,  7.04985815,  7.04278354, ...,
#       7.03571603, 7.04278354,  7.04985815],
#     ...,
#     [ 7.04988652,  7.04279774,  7.03571603, ...,
#       7.0286414 , 7.03571603,  7.04279774],
#     [ 7.05693985,  7.04985815,  7.04278354, ...,
#       7.03571603, 7.04278354,  7.04985815],
#     [ 7.06400028,  7.05692568,  7.04985815, ...,
#       7.04279774, 7.04985815,  7.05692568]
# ])

def plotVectorizationExample():
    """
    using matplotlib.pyplot.imshow to create image
    from 2D array of: xs**2+ys**2
    
    xs,ys = np.meshgrid(np.arange(-5,5,0.01))
    np.sqrt(xs**2 + ys**2)
    """
    plt.imshow(
        z, cmap=plt.cm.gray
    )
    plt.colorbar()
    plt.title(
        "Image plot of $\sqrt{x^2 + y^2}$ for a grid of values"
    )
    plt.show()
    plt.savefig("ch4_SqrtOfSum_xSquared_ySquared.png")


