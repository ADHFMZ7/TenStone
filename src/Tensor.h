#ifndef TENSOR_H
#define TENSOR_H

#include <functional>
#include <iostream>
#include <numeric>
#include <vector>
#include <ranges>
#include <cstdlib>

// For now im making this only work with floats.

template <typename T>
class Tensor {

public:

  explicit Tensor(std::vector<int> shape) {

    this->size = std::reduce(shape.begin(), shape.end(), 1, std::multiplies<int>{});

    buffer.resize(this->size);

  }

  // Static factory method to create tensor filled with random data
  static Tensor Rand(std::vector<int> shape, float min=0, float max=1) {

    // if (std::is_same(T, int)) {
    //
    // }

    std::srand(std::time(nullptr));

    auto new_t = Tensor(shape);
    for (int i = 0; i < new_t.size; i++) {
      new_t.buffer[i] = (float)rand()/(float)(RAND_MAX/max);
    }
    std::cout << new_t.buffer[10];
    return new_t;
  }

  ~Tensor() {
    // Dealocates memory
    buffer.clear();
  }

  Tensor item() const;

  std::vector<T> buf() const {return buffer;}
  int get_size() const {return size;}

  Tensor add(Tensor b) {

    if (this->shape != b.shape) {
      // throw exception
    }
    
    auto c = Tensor(this->shape);
    std::cout << c.buffer[0] << std::endl; 
    for (int i = 0; i < this->size; i++) {
      c.buffer[i] = this->buffer[i] + b.buffer[i];
    }
    return c;
  }

  T& operator[](int index) {
    return this->buffer[index];
  }

  T& operator[](std::vector<int> indices) {
    if (indices.size() != this->size) {
      // throw error
    }
     

  }


private:

  int size;
  std::vector<T> buffer;

  std::vector<int> strides; 
  std::vector<int> shape;  
  
};


#endif
