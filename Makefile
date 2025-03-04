# Compiler and Flags
CXX := g++
CXXFLAGS := -O3 -Wall -shared -std=c++11 -fPIC -arch arm64

# Python Config
PYTHON_INCLUDE := $(shell python3-config --includes)
PYTHON_LIBS := $(shell python3-config --ldflags)

# Pybind11 Include Path
PYBIND11_INCLUDE := extern/pybind11/include

# Source and Output
SRC := src/tensor.cpp
OUT := ./tensor$(shell python3-config --extension-suffix)

# Build Rule
all: $(OUT)

$(OUT): $(SRC)
	$(CXX) $(CXXFLAGS) $(PYTHON_INCLUDE) -I$(PYBIND11_INCLUDE) \
		$< -o $@ $(PYTHON_LIBS) -Wl,-undefined,dynamic_lookup

# Clean Build Artifacts
clean:
	rm -f $(OUT)
