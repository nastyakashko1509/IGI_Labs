import numpy as np

class WorkingWithMatrices:
    def replacement_of_the_largest_elements(self, matrix):
        """  Замена мест наибольших элементов в первом и последнем столбцах.  """

        first_column = matrix[:, 0]   
        last_column = matrix[:, -1]   
        
        max_first = np.max(first_column)  
        max_last = np.max(last_column)    
        
        matrix[:, 0][matrix[:, 0] == max_first] = max_last        
        matrix[:, -1][matrix[:, -1] == max_last] = max_first
        
        return matrix
    
    def definition_of_correlation_coefficient(self, matrix):
        """  Определение коэффициента корреляции между элементами первого и последнего столбца.  """

        first_column = matrix[:, 0]   
        last_column = matrix[:, -1] 

        correlation_matrix = np.corrcoef(first_column, last_column)
        correlation = round(correlation_matrix[0, 1], 2) 

        return(correlation)