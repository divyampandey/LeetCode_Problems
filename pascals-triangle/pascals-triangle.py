class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

            output_array = [[1],[1,1]]
            ans_array = []
            n = numRows
            if n == 1:            
                ans_array.append(output_array[0])
                return ans_array

            elif n == 2:
                ans_array.extend(output_array[:2])
                return ans_array
            else:
                for i in range(3,n+1):
                    
                    temp = output_array[i-2]
                    t = [1]
                    for j in range(len(temp)-1):
                        sm = temp[j] + temp[j+1]
                        t.append(sm)
                    t.append(1)
                    output_array.append(t)
                ans_array.extend(output_array)
                return ans_array
                        
                    
            
            