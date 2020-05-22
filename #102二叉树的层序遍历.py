# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:47:52 2020

@author: Administrator
"""

"""本题题解为BFS
自己做的时候就用递归并且每次记录深度将当前深度下的节点加入二维数组当中
看了题解之后发现这题涉及到了BFS，用一个队列来辅助进行层序遍历
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        List = []
        self.Add_k(root,List,0)
        return List
        
    def Add_k(self,root,List,k):
        if root:
            if len(List)<=k:
                List.append([])
            List[k].append(root.val)
        else:
            return
        #print(List)
        self.Add_k(root.left,List, k+1)
        self.Add_k(root.right,List, k+1)

import queue
"""下面为BFS的代码"""
class Solution(object):
    def levelOrder(self, root):
        out=[]
        if root == None:
            return []
        Q=queue.Queue()
        Q.put(root)
        while Q.empty()!=True:
            level = []
            k = Q.qsize()
            for i in range(k):
                node = Q.get()
                if node:
                    level.append(node.val)
                    Q.put(node.left)
                    Q.put(node.right)
                    #print(node.val)
            out.append(level)
        return out[0:-1]
        
Tree = TreeNode(3)
Tree.left = TreeNode(9)
Tree.right = TreeNode(20)
Tree.right.left = TreeNode(15)
Tree.right.right = TreeNode(7)
print(Solution().levelOrder(Tree))