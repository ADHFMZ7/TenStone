#include "tensor.h"

template <typename T>
Tensor<T>::Tensor(std::vector<int> shape) {

    this->size = std::reduce(shape.begin(), shape.end(), 1, std::multiplies<int>{});

    std::cout << this->size << std::endl;

    // buffer.reserve(this->size);
    buffer.resize(this->size);

}

template <typename T>
Tensor<T>::~Tensor() {
  buffer.clear();
}

template <typename T>
std::vector<T> Tensor<T>::buf() const {
  return buffer;
}

// Implement this one later
template <typename T>
Tensor<T> Tensor<T>::item() {
  return this;
}
