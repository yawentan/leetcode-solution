# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:24:47 2020

@author: Administrator
"""

"""没有考虑t字符串有重叠字符"""
class Solution1(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        Hashmap = {}
        MinLen = len(s)
        MinStart = 0
        for i in t:
            Hashmap[i].append(-1)
        print(Hashmap)
        for i in range(len(s)):
            #更新hashmap中的元素坐标
            if Hashmap.get(s[i]) != None:
                #入hash
                Hashmap[s[i]] = i
                #找出不含s[i]的当前最小
                Min = self.find(Hashmap,s[i],i)
                if Min!=None and MinLen > i - Min + 1:
                    MinLen = i - Min + 1
                    MinStart = Min
                #print(Hashmap,Min,MinLen,MinStart)
        for value in Hashmap.values():
            if value == -1:
                return ""
        #print(MinStart,MinLen)
        return s[MinStart:MinStart+MinLen]
    
    def find(self,Hashmap,ch,i):
        for value in Hashmap.values():
            if value == -1:
                return 
        Min = i
        for key in Hashmap.keys():
            if key != ch:
                Min = min(Hashmap[key],Min)
        return Min
    
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        Hashmap = {}
        MinLen = len(s)
        MinStart = 0
        Min = -1
        Flag = 0
        self.Count = 0#记录压入次数
        for i in t:
            Hashmap[i] = []
        for i in t:
            Hashmap[i].append(-1)
        #每进来一个元素，替换掉其中最小的
        for i in range(len(s)):
            Min = self.UpdataHash(Hashmap,s[i],i)
            #存在完整的子串
            #print(Hashmap,i,Min,MinLen)
            if Min!=-2 and Min!=-1:
                #print(Hashmap,i,Min,MinLen)
                Flag = 1
                if MinLen > i - Min + 1:
                    MinLen = i - Min + 1
                    MinStart = Min
            
        #判断是否不存在匹配字符串
        if Flag:
            return s[MinStart:MinStart+MinLen]
        else:
            return ""
    
    def UpdataHash(self,Hashmap,ch,i):
        if Hashmap.get(ch)==None:
            return -2
        Hashmap[ch].pop(0)
        Hashmap[ch].append(i)
        Min = Hashmap[ch][0]
        for key in Hashmap.keys():
            Min = min(Hashmap[key][0],Min)
        return Min#返回修改元素最小值
s = "ab"
t = "a"  
print(Solution().minWindow(s,t))
