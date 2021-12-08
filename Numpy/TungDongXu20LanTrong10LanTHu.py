import numpy as np         
coins = np.random.binomial(20, 0.5, 10) # Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp
print(" số lần tung được mặt ngửa: ", coins)
# số lần tung được mặt ngửa:  [ 7 10 11 10 10  5 11  9 10 14]