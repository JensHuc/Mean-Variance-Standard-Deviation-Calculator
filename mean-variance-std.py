import numpy as np

list = [2,6,2,8,4,0,1,5]

if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
else:
    a = np.array(list).reshape(3,3)
    
    mean1 = a.mean(axis=0)
    mean1 = mean1.tolist()
    mean2 = a.mean(axis=1)
    mean2 = mean2.tolist()
    mean = a.mean()
    
    var1 = a.var(axis=0)
    var1 = var1.tolist()
    var2 = a.var(axis=1)
    var2 = var2.tolist()
    var = a.var()
    
    std1 = a.std(axis=0)
    std1 = std1.tolist()
    std2 = a.std(axis=1)
    std2 = std2.tolist()
    std = a.std()
    
    max1 = a.max(axis=0)
    max1 = max1.tolist()
    max2 = a.max(axis=1)
    max2 = max2.tolist()
    max0 = a.max()
    
    min1 = a.min(axis=0)
    min1 = min1.tolist()
    min2 = a.min(axis=1)
    min2 = min2.tolist()
    min0 = a.min()
    
    sum1 = a.sum(axis=0)
    sum1 = sum1.tolist()
    sum2 = a.sum(axis=1)
    sum2 = sum2.tolist()
    sum0 = a.sum()
    
    
    calculations = {'mean': [mean1, mean2, mean],
                    'variance': [var1, var2, var],
                    'standard deviation': [std1, std2, std],
                    'max': [max1, max2, max0],
                    'min': [min1, min2, min0],
                    'sum': [sum1, sum2, sum0]}
print(calculations)
    


    