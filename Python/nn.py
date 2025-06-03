inputs = [1,2,3,4]
weights = [2,4,6,8]
bias = 5

output = 0
for inpt, weight in zip(inputs, weights):
    output += inpt * weight
output += bias
print(output)
