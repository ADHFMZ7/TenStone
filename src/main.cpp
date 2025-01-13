#include "tensor.h"
#include <iostream>
#include <vector>

// Example of how I want the lib to be used


int main() {

  auto size = std::vector<int>{10, 10, 5};

  auto ten = Tensor<float>(size);

  auto rand_ten = Tensor<float>::Rand(size);
  auto buf = rand_ten.buf(); 

  std::cout << buf.size() << std::endl;

  for (int i = 0; i < buf.size(); i++) {
    std::cout << buf[i] << std::endl;
  }

}
