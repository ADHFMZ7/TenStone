"""
Implements the Tensor class.

TODO:
    Make sure numpy error handling works
    Write unit tests
    Add documentation 

"""
import numpy as np



class Tensor:

    def __init__(self, data, _children=()):
        if isinstance(data, list):
            data = np.array(data, dtype=np.single)
        elif not isinstance(data, np.ndarray):
            raise ValueError("Input data must be a NumPy array")

        # Information for autograd
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_children)

        self.data = data

    @property
    def shape(self):
        return self.data.shape

    @property
    def size(self):
        return self.data.size

    def get(self, indices):
        print(self.data, indices)
        return self.data[tuple(indices)]

    def set(self, indices, value):
        self.data[tuple(indices)] = value

    def __repr__(self):
        return self.data.__str__()

    def __getitem__(self, indices):
        return self.get(indices)

    def __setitem__(self, indices, new_value):
        self.set(indices, new_value)

    

# Unary Ops

    def sum(self):

        ret = Tensor(self.data.sum(keepdims=True).squeeze(), _children=(self, ))

        def _backward():
            self.grad = np.ones_like(self.data)

        ret._backward = _backward
        return ret

# Binary Ops

    def dot(self, other):
      
        ret = Tensor(np.dot(self.data, other.data), _children=(self, other))

        def _backward():

            print(self.shape, other.shape, ret.shape)

            self.grad = ret.grad @ other.data.T
            other.grad = self.data.T @ ret.grad

        ret._backward = _backward
        return ret



# CONSTRUCTORS

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


    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        self.grad = 1
        for v in reversed(topo):
            v._backward()

if __name__ == "__main__":
    A = Tensor([[1, 2, 3], [4, 5, 6]])
    B = Tensor([[1, 2], [3, 4], [5, 6]])

    C = A.dot(B)
    D = C.sum()
    D.backward()



    print(A.grad)
    print(B.grad)
    print(C.grad)
