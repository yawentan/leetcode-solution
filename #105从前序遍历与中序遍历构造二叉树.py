# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:03:09 2020

@author: Administrator
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def preorder(self):
        if self:
            print(self.val)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.val)
            if self.right:
                self.right.inorder()
"""之前T了,主要是分preorder不对，可以利用分裂后inorder的长度来分preorder"""
"""修改之后过了的版本"""
class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #print(preorder, inorder,len(preorder))
        if len(preorder) == 0:
            return 
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        LefttInorder = inorder[0:root_idx]
        RightInorder = inorder[root_idx+1:]
        
        LeftPreorder = preorder[1:root_idx+1]
        RightPreorder = preorder[root_idx+1:]
        Tree = TreeNode(preorder[0])
        #print(preorder[0])
        Tree.left = self.buildTree(LeftPreorder,LefttInorder)
        Tree.right = self.buildTree(RightPreorder,RightInorder)
        return Tree


"""
从左向右遍历preorder，将其中每个节点都当成根节点，split inorder当分离出来的
inorder为空或者为1时，返回None和TreeNode(inorder[0])
这个方法是开始为了解决不好分preorder才想出来的，看了官方题解之后，发现好好分preorder
一点事没有
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return
        self.i = 0
        r = inorder.index(preorder[self.i])
        self.i+=1
        root = TreeNode(inorder[r])
        root.left = self.findleft(inorder[0:r],preorder)
        root.right = self.findright(inorder[r+1:],preorder)
                
        return root
    def findleft(self,inorder,preorder):
        #print(inorder,self.i)
        if len(inorder) == 0:
            return
        if len(inorder) == 1:
            self.i+=1
            return TreeNode(inorder[0])
        r = inorder.index(preorder[self.i])
        self.i+=1
        root = TreeNode(inorder[r])
        root.left = self.findleft(inorder[0:r],preorder)
        root.right = self.findright(inorder[r+1:],preorder)
        return root
    def findright(self,inorder,preorder):
        #print(inorder,self.i)
        if len(inorder) == 0:
            return
        if len(inorder) == 1:
            self.i+=1
            return TreeNode(inorder[0])
        r = inorder.index(preorder[self.i])
        self.i+=1
        root = TreeNode(inorder[r])
        root.left = self.findleft(inorder[0:r],preorder)
        root.right = self.findright(inorder[r+1:],preorder)
        
        return root
        
preorder = [3,9,20,15,7]
inorder =  [9,3,15,20,7]
Tree = Solution2().buildTree(preorder,inorder)
Tree.inorder()
Tree.preorder()
