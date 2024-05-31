"""
Implements the Tensor class.

"""
import numpy as np


class Tensor:

    def __init__(self, shape):
        # if valid_shape
        self.data = np.random.randn(*shape)


    @classmethod
    def zeros(cls, shape):
        ret = cls(shape)
        ret.data = np.zeros(shape)
        return ret
        

    @classmethod
    def ones(cls, shape):
        ret = cls(shape)
        ret.data = np.ones(shape)
        return ret
      
    @classmethod
    def from_data(cls):
        ...


if __name__ == "__main__":
    a = Tensor.ones((10, 10))
    b = Tensor.zeros(a.data.shape)
    print(a.data)
    print(b.data)
