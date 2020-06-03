# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 09:05:04 2020

@author: Administrator
"""

"""本来是o(N*W)，通过前缀和优化到o(N)"""
"""题解用的从后往前的差分的方法来通过o(1)的时间来获得P(i)等价于我的前缀和"""
class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        C = 10**5
        P = [0.0]*(N+1)
        P[0] = 1.0
        Pre = [0.0]*(N+2)
        count = 0
        for i in range(N+1):
            P[i]+=Pre[i]/W
            #print(P[i])
            if i<K:
                Pre[i+1] = Pre[i] + P[i]
                count+=1
            else:
                Pre[i+1] = Pre[i]
                count+=1
                
            if count == W+1:
                count-=1
                Pre[i+1] -= P[i-W]
        Sum = 0.0
        #print(Pre)
        for i in range(K,N+1):
            Sum+=P[i]*C
       # print(Sum/C)
        return Sum/C
      
N=9811
K=8776
W=1096
Solution().new21Game(N, K, W)