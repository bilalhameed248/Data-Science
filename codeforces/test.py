hash_table = {
    'name1': 'xyz',
    'name2': 'xyz1',
    'name3': 'xyz3'
}
class Node:
    def __init__(self, data):
        self.data = data 
        self.next_node = None
a = Node(1)
b = Node(2)
c = Node(3)
a.next_node = b 
b.next_node = c 
print(a.next_node)