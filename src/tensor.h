#ifndef TENSOR_H
#define TENSOR_H

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <functional>
#include <iostream>
#include <numeric>
#include <cstdlib>
#include <vector>
#include <ranges>

namespace py = pybind11;
// For now im making this only work with floats.


template <typename T>
class Tensor {

public:

  explicit Tensor(std::vector<int> shape) {
    size_ = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<int>());
    buffer_.resize(size_);
  }

  // Static factory method to create tensor filled with random data
  static Tensor Rand(std::vector<int> shape, float min=0, float max=1) {

    // if (std::is_same(T, int)) {
    //
    // }

    std::srand(std::time(nullptr));

    auto new_t = Tensor(shape);
    for (int i = 0; i < new_t.size_; i++) {
      new_t.buffer_[i] = (float)rand()/(float)(RAND_MAX/max);
    }
    std::cout << new_t.buffer_[10];
    return new_t;
  }

  static Tensor Zeros(std::vector<int> shape) {
    auto new_t = Tensor(shape);
    for (int i = 0; i < new_t.size_; i++) {
      new_t.buffer_[i] = 0;
    }
    return new_t;
  }

  static Tensor Ones(std::vector<int> shape) {
    auto new_t = Tensor(shape);
    for (int i = 0; i < new_t.size_; i++) {
      new_t.buffer_[i] = 1;
    }
    return new_t;
  }

  static Tensor Eye(int n) {
    auto new_t = Tensor({n, n});
    for (int i = 0; i < n; i++) {
      new_t.buffer_[i*n + i] = 1;
    }
    return new_t;
  }

  static Tensor Arange(int start, int end, int step=1) {
    // datatypes work a bit different here, need to fix
    auto new_t = Tensor<int>({(end-start)/step});
    for (int i = 0; i < new_t.size_; i++) {
      new_t.buffer_[i] = start + i*step;
    }
    return new_t;
  }

  // static Tensor<double> Linspace(double start, double end, int n) {
  //   auto new_t = Tensor<double>({n});
  //   for (int i = 0; i < n; i++) {
  //     new_t.buffer_[i] = (start + i*(end-start)/(n-1));
  //   }
  //   return new_t;
  // }

  ~Tensor() {
    // Dealocates memory
    buffer_.clear();
  }

  Tensor item() const;

  std::vector<T> buf() const {return buffer_;}
  int get_size() const {return size_;}

  Tensor add(Tensor b) {

    if (shape_ != b.shape_) {
      // throw exception
    }
    
    auto c = Tensor(shape_);
    std::cout << c.buffer_[0] << std::endl; 
    for (int i = 0; i < size_; i++) {
      c.buffer_[i] = buffer_[i] + b.buffer_[i];
    }
    return c;
  }

  T& operator[](int index) {
    return buffer_[index];
  }

  T& operator[](std::vector<int> indices) {
    if (indices.size() != size_) {
      // throw error
    }

  }



// Arithmetic Operators

  Tensor<T> operator+(Tensor<T> const& other) {
    // Ensure the tensors have compatible sizing
    // Later this will take into account possible broadcasting
    auto c = Tensor<T>(shape_);

    if (size_ == other.get_size()) {
      for (int ix = 0; ix < size_; ++ix) {
          c[ix] = this[ix] + other[ix];
      }
    }
    return c;
  }

  // Tensor<T> operator


private:

  int size_;
  std::vector<T> buffer_;

  std::vector<int> strides_;
  std::vector<int> shape_;
  
};


PYBIND11_MODULE(tensor, m) {
    py::class_<Tensor<float>>(m, "Tensor")
        .def(py::init<std::vector<int>>())
        .def("get_size", &Tensor<float>::get_size);
}

#endif
