import unittest
import tensor as ts
import torch

class TestAbsFunction(unittest.TestCase):


    def test_addition_gradient(self):

        A_t = torch.rand(10, 10)
        A_b = ts.Tensor(A_t.numpy())
       
        B_t = torch.rand(10, 10)
        B_b = ts.Tensor(A_t.numpy())
       
        C_t, C_b = A_t + B_t, A_b + B_b

        print(A_t, "\n")

        print(A_b)

        self.assertEqual(C_t.numpy(), C_b.data)


if __name__ == "__main__":
    unittest.main()
