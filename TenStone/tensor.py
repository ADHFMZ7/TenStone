"""
Implements the Tensor class.

"""


class Tensor:

    def __init__(self, shape):
        # if !valid_shape(shape):
            # raise Exception("Invalid shape") 

        def dfs(ix):
            if ix >= len(shape) - 1:
                return [0 for _ in range(shape[ix])]

            return [dfs(ix + 1) for _ in range(shape[ix])]

        print(dfs(0))

        self.data = []
        

    @classmethod
    def zeros(cls, shape):
        pass
        # ret = cls(shape)
        # ret.data = np.zeros(shape)
        # return ret
        

    @classmethod
    def ones(cls, shape):
        pass
        # ret = cls(shape)
        # ret.data = np.ones(shape)
        # return ret
      
    @classmethod
    def from_data(cls):
        ...


if __name__ == "__main__":
    Tensor([2, 2])
    # a = Tensor.ones((10, 10))
    # b = Tensor.zeros(a.data.shape)
