#include "tensor.h"
#include <iostream>
#include <vector>

// Example of how I want the lib to be used


int main() {

  auto size = std::vector<int>{10, 10, 5};

  auto A = Tensor<double>::Rand(size, 0, 100);

  auto range = Tensor<double>::Linspace(-1, 1, 15);

  for (int i = 0; i < A.get_size(); i++) {
    std::cout << A[i] << std::endl;
  }

  auto B = Tensor<double>::Rand(size, 0, 100);

  A + B;

}
