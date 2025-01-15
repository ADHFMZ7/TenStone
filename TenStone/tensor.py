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
            self.grad += np.ones_like(self.data)

        ret._backward = _backward
        return ret

# Binary Ops

    def dot(self, other):
      
        ret = Tensor(np.dot(self.data, other.data), _children=(self, other))

        def _backward():

            self.grad += ret.grad @ other.data.T
            other.grad += self.data.T @ ret.grad

        ret._backward = _backward
        return ret


    def __add__(self, other):
        # Put this in a function later
        # if isinstance(other, Tensor):
        #     ...
        # elif isinstance(other, float) or isinstance(other, int):
        #     other = Tensor(other)
        # elif isinstance(other, )
        # else:
        #     raise TypeError("Invalid type for tensor operation add")
            
        ret = Tensor(self.data + other.data, _children=(self, other)) 

        def _backward():
            self.grad += ret.grad
            other.grad += ret.grad

        ret._backward = _backward
        return ret

    def __mul__(self, other):


        ret = Tensor(self.data * other.data, _children=(self, other))

        def _backward():
            pass 

        ret._backward = _backward
        return ret

# CONSTRUCTORS

    @classmethod
    def zeros(cls, *shape, requires_grad=False):
        ret = cls(np.zeros(*shape))
        return ret

    @classmethod
    def ones(cls, *shape, requires_grad=False):
        ret = cls(np.ones(*shape))
        return ret

    @classmethod
    def eye(cls, *shape, requires_grad=False):
        ret = cls.zeros(*shape)
        for i in shape:
            for j in range(i):
                ret[i]

        return ret

    @classmethod
    def randn(cls, *shape, requires_grad=False):
        ret = cls(np.random.randn(*shape))
        return ret

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

