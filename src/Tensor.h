#ifndef TENSOR_H
#define TENSOR_H

#include <vector>

class Tensor {

public:

  Tensor() {

    buffer.reserve(this->size);

  }

  ~Tensor() {
    // Dealocates memory

    buffer.clear();

  }

  Tensor item();



private:

  int size;
  std::vector<float> buffer;


  std::vector<int> strides; 
  int shape; 
  

  
};


#endif
