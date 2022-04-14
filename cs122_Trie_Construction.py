import pandas as pd


class Node:
    def __init__(self, data):
        self.children = []
        self.data = data



'''
newList = []
for i in range(0, len(PatternsList)):
    newList.append(PatternsList[i][0])


def TrieConstruction(newList):
    dict = {}

    for i in newList:  # For each string pattern in patterns
        currentNode = Node(0)
        currentString = newList[i][0]

        for j in range(0, len(currentString) - 1):
            currentSymbol = currentString[j]

            if len(currentNode.children) == 0: # if there are no edges for current node
                newNode = Tree(str(j+1))
                dict[currentNode.data + newNode.data] = currentSymbol
                currentNode = newNode


                for k in dict.items() :
                    if k == currentSymbol: #if theres an edge from current node with current symbol
                        currentNode = k[1] # key of dict should be two char string with [0] = intial node and [1] = terminal node
                    else:
                        newNode = Tree(j+1)
                        currentNode.children.append(str(newNode.data) + currentSymbol)
                        currentNode = newNode

    return dict



output = TrieConstruction(Patterns)

print(output.children)
print(1.children)
'''
_end = '_end_'
def make_trie(*words):

    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict = current_dict.setdefault(_end, _end)
    return root


def trie_tostr(root):
    s = []
    def dump_leaf(curr,parent_id):
        current_id = parent_id + 1
        for key, value in curr.items():
            if (value == _end):
                continue
            s.append(str(parent_id)+'->'+str(current_id)+':'+key)
            current_id = dump_leaf(value,current_id)
        return current_id
    dump_leaf(root,0)
    return '\n'.join(s)


fname = '/Users/Caden/Downloads/dataset_317406_4-2.txt'
with open(fname, "r") as f:
    words = f.read().splitlines()

t = make_trie(*words)
s = trie_tostr(t)
with open(fname+'out', "w") as f:
    f.write(s)