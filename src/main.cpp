#include "tensor.h"
#include <iostream>
#include <vector>

// Example of how I want the lib to be used


int main() {

  auto size = std::vector<int>{10, 10, 5};


  auto a = Tensor<float>::Rand(size);
  auto b = Tensor<float>::Rand(size);

  auto c = a.add(b);

  for (int i = 0; i < a_buf.size(); i++) {
    std::cout << a_buf[i] << " + " << b_buf[i] << " = " << c_buf[i] << std::endl;
  }

}
