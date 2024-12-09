# GeMU: MIMO Activation function via cone projection

This Python package implements the **GeMU (Generalized Multivariate projection Unit)** model using PyTorch. It is designed to process multi-dimensional input data using a **cone-based projection** method. The package includes a class `soc`, which can be used for various computations such as dimensional projection, angle adjustments, and norm-based filtering.

This activation function is proposed in the paper [Generalized Activation via Multivariate Projection](https://arxiv.org/abs/2309.17194).

## Installation

You can install the GeMU package using `pip` or by cloning the repository.

### Using `pip`
Once your package is uploaded to PyPI, you can install it with:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps GeMU
```

## Usage
### Importing and Initializing

To use the package, import the `soc` class and initialize it with the appropriate parameters.
```python
import torch
from GeMU import soc

# Initialize the model
model = soc(cone_dim=2)

# Define input tensor (batch_size * (width * height) * feature_dimension)
x = torch.randn(8, 16, 64).cuda()  # Example tensor
output = model(x)
```

### Model Description

The `soc` class implements a neural network module that operates on multi-dimensional input data. It projects input features onto a cone space and performs norm-based operations with several configurable parameters.

#### Key Parameters:
- `angle_tan`: The initialization of the tangent of the cone's half-apex angle. Default is 1.
- `cone_dim`: The dimensionality of the cone projection. Usually set to 2 or 3.

#### Key Methods:
- `forward(x)` as in pytorch:
    - `x`: Input tensor with shape (batch_size, width * height, feature_dimension). The feature dimension must be the last dimension.
    - The method reshapes the input data, applies cone projections, and computes an output tensor based on certain geometric conditions.

### Examples

Here’s a complete example of how to use the `soc` class:
```python
import torch
from GeMU import soc

# Initialize the model with a specified tan(angle) and cone dimension
model = soc(cone_dim=2)

# Example input: batch_size = 8, feature dimension = 64, cone projection in 2D
x = torch.randn(8, 16, 64).cuda()

# Compute the result by passing the input through the model
output = model(x)

# Output shape and content
print(output.shape)  # Output shape based on input and model operations

```

### Dependencies
- `PyTorch`: The package relies on PyTorch for tensor operations and GPU support.
- `NumPy`: Used for numerical operations like square roots and norms.

### License
This project is licensed under the MIT License - see the LICENSE file for details.  

## Contact
For any questions or issues, please reach out to lijiayun22@mails.tsinghua.edu.cn.
