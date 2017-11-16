# coding=utf-8
# 二叉树的实现


class BinerayTree(object):
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None

    def insertleft(self, new_node):
        if not self.leftchild:
            self.leftchild = BinerayTree(new_node)

        else:
            t = BinerayTree(new_node)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self, new_node):
        if not self.rightchild:
            self.rightchild = BinerayTree(new_node)
        else:
            t = BinerayTree(new_node)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getrightchild(self):
        return self.rightchild

    def getleftchild(self):
        return self.leftchild

    def setrootval(self, obj):
        self.key = obj

    def getrootval(self):
        return self.key


