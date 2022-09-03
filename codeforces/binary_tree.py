class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data >  self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def SearchItem(self, x):
        if self.data:
            if x==self.data:
                found=True
                return found
            if x < self.data:
                if self.left is None:
                    found=False
                    return found
                return self.left.SearchItem(x)
            elif x > self.data:
                if self.right is None:
                    found=False
                    return found
                return self.right.SearchItem(x)
        else:
            found=False
            return found

    def InOrderTraversal(self, root):
        res=[]
        if root:
            res=self.InOrderTraversal(root.left)
            res.append(root.data)
            res=res+self.InOrderTraversal(root.right)
        return res

    def PreOrderTraversal(self, root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.PreOrderTraversal(root.left)
            res=res+self.PreOrderTraversal(root.right)
        return res

if __name__=='__main__':
    root=Node(12)
    root.insert(55)
    root.insert(18)
    root.insert(3)
    root.insert(33)
    root.PrintTree()
    result=root.SearchItem(21)
    if result==True:
        print("Found")
    else:
        print("Not Found")
    
    res=root.InOrderTraversal(root)
    print(res)
    res=root.PreOrderTraversal(root)
    print(res)



