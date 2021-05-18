import numpy as np

class Perceptron:
  def __init__(self,input_length,weights=None):
    if weights is None:
      #print("Debugging")
      self.weights=np.ones(input_length)*0.5 
    else:
      #print("Debugging2")
      self.weights=weights
      #print(self.weights)
      
  def unit_step_function(x):
    if x>0.5:
      return 1
    return 0
  def __call__(self,in_data):
    #print("Debugging in call method")
    #print("Inputs",in_data)
    weighted_input=self.weights*in_data
    #print("weighted input =",weighted_input)
    weighted_sum=weighted_input.sum()
    #print("weighted sum=",weighted_sum)
    #print("summation of weighted sum",weighted_sum)
  
    return Perceptron.unit_step_function(weighted_sum)


# WITHOUT BIASNESS
print("Printing without biasness")
p = Perceptron(2, np.array([0.5,0.5]))
for in1 in range(2):
  for in2 in range(2):
    data_in = (in1,in2)
    data_out = p(data_in)
    print(data_in,data_out)


#ADDED WEIGHTS OF BIAS AND ADDED BIAS IN INPUT 
print()
print("Printing the same perceptron with biasness adding")
p = Perceptron(3, np.array([0.5,0.5,0.5]))
in3=1
for in1 in range(2):
  for in2 in range(2):
    data_in = (in1,in2,in3)
    data_out = p(data_in)
    print(data_in,data_out)

