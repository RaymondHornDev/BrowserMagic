import random

class Node:
    '''Data storage node for binary tree'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
class CreateTree:
    '''Creates a binary tree'''
    def __init__(self):
        self.root = None
        
    def add_node(self, value):
        '''Tests for and stores root node'''
        if self.root is None:
            self.root = Node(value)
            print('Root Stored')
        else:
            self.place_node(self.root, value)

    def place_node(self, current, value):
        '''Locates the proper postiion based on value and position of other nods to insert new node'''
        print(value)
        if value < current.value:
            if current.left is None:
                print('New node left')
                current.left = Node(value)
            else:
                print('Moving left')
                self.place_node(current.left, value)
                
        else:
            if current.right is None:
                print('New node right')
                current.right = Node(value)
            else:
                print('Moving Right')
                self.place_node(current.right, value)
                
                
    def get_root(self):
        '''Returns value of root node'''
        return self.root
                
    def inorder(self, current):
        '''Inorder traversal'''
        if current.left:
            self.inorder(current.left)
            
        print(current.value)
        
        if current.right:
            self.inorder(current.right)
            
    def preorder(self, current):
        '''Preorder traversal'''
        print(current.value)
        
        if current.left:
            self.preorder(current.left)
            
        if current.right:
            self.preorder(current.right)
            
    def postorder(self, current):
        '''Post order traversal'''
        if current.left:
            self.postorder(current.left)
            
        if current.right:
            self.postorder(current.right)
        
        print(current.value)
            
            

ct = CreateTree()      
   
for iter in range(50):
    rand_int = random.randint(0, 101)
    ct.add_node(rand_int)
    
r = ct.get_root()
ct.inorder(r)
print('\n\n')
ct.preorder(r)
print('\n\n')
ct.postorder(r)
print('\n\n')
print(ct.root.value)