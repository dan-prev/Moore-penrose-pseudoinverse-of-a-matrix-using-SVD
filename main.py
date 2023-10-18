#Function to calculate the pseudoinverse of a matrix
  def moore_penrose_pseudoinverse(matrix):
    #Performing Singular Value Decomposition (SVD)
    U, S, VT = np.linalg.svd(matrix, full_matrices = True)
    
    #Calculate the reciprocal (1/x) of a non-zero singular value
    reciprocal_singular_values = 1.0/S
    
    #Create an empty matrix filled with zeros
    Sigma_plus = np.zeros(matrix.shape)

    #Fill the top-left part of the blank canvas with the reciprocal
    for i in range(len(S)):
      Sigma_plus[i, i] = reciprocal_singular_values[i]
      
    #Compute pseudoinverse using formula
    pseudoinverse = np.dot(VT.T, np.dot(Sigma_plus, U.T))
    
    #Return the pseudoinverse matrix as a result
    return pseudoinverse

#Loop for every trial
for i in range(N):
  #Generate a random square matrix
  n = np.random.rantint(1,10)
  A = np.random.rand(n,n)
  
  #Ensure invertible by adding diagonal term
  A += 0.25 * np.eye(n)
  
  #Compute standard matrix inverse
  A_inv = np.linalg.inv(A)
  
  #Calculate pseudoinverse using our function
  A_pseudoinv = moore_penrose_pseudoinverse(A)

  #Verify if the pseudoinverse is approximately equal to the inverse
  if np.allclose(A_pseudoinv, A_inv):
    print("Test passed for trial", i)
  else:
    print("Test failed for trial", i)

print("All tests completed!")