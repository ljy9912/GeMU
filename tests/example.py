import torch
from GeMU import soc

model = soc(angle_tan=1.19, cone_dim=2)

# Example input: batch_size = 8, feature dimension = 64, cone projection in 2D
x = torch.randn(8, 16, 64).cuda()

# Compute the result by passing the input through the model
output = model(x)

# Output shape and content
print(output.shape)  # Output shape based on input and model operations