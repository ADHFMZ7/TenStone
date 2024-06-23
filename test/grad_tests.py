import unittest
import TenStone.tensor as ts
import torch

class TestAbsFunction(unittest.TestCase):


    def test_addition_gradient(self):

        A_t = torch.rand(100, 100)
        A_b = ts.Tensor(A_t.numpy())
       
        B_t = torch.rand(100, 100)
        B_b = ts.Tensor(A_t.numpy())
       
        C_t, C_b = A_t @ B_t, A_b.dot(B_b)

        self.assertEqual(C_t, C_b)


if __name__ == "__main__":
    unittest.main()
