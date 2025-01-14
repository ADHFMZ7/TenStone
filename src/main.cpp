#include "tensor.h"
#include <iostream>
#include <vector>

// Example of how I want the lib to be used


int main() {

  auto size = std::vector<int>{10, 10, 5};


  auto a = Tensor<float>::Rand(size);
  auto b = Tensor<float>::Rand(size);

  auto c = a.add(b);

  for (int i = 0; i < a.get_size(); i++) {
    std::cout << a[i] << " + " << b[i] << " = " << c[i] << std::endl;
  }

}
