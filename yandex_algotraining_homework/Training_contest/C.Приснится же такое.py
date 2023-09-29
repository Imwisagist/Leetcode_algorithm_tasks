# https://contest.yandex.ru/contest/50668/enter

class Tree:
    class Node:
        def __init__(self, _value: int):
            self.value = _value
            self.parent = self.left = self.right = None

        def __str__(self):
            return "value: " + str(self.value) + \
                "\nparent: " + str(self.parent) + \
                "\nleft: " + str(self.left) + \
                "\nright: " + str(self.right)
        
    def __init__(self, N: int):
        self.N, self.root, self.nodes = N, 1, [None]

        for i in range(1, self.N+1):
            node = self.Node(i); parent = i // 2

            if parent > 0:
                node.parent = self.nodes[parent].value

                if self.nodes[parent].left is None:
                    self.nodes[parent].left = i
                else: self.nodes[parent].right = i

            self.nodes.append(node)

    def print(self) -> None: self.__in_order(self.root)

    def __in_order(self, v: int) -> None:
        if self.nodes[v].left: self.__in_order(self.nodes[v].left)

        print(self.nodes[v].value, end=' ')

        if self.nodes[v].right: self.__in_order(self.nodes[v].right)

    def swap(self, v: int) -> None:
        if self.root == v: return
        
        p = self.nodes[v].parent

        if self.nodes[p].parent is not None:
            pp = self.nodes[p].parent

            if self.nodes[pp].left == p: self.nodes[pp].left = v
            else: self.nodes[pp].right = v

            self.nodes[v].parent = pp
        else:
            self.root = v; self.nodes[v].parent = None

        if self.nodes[p].left == v: self.__left_swap(v, p)
        else: self.__right_swap(v, p)

    def __left_swap(self, v: int, p: int) -> None:
        left_tree = self.nodes[v].left; self.nodes[v].left = p
        self.nodes[p].parent = v; self.nodes[p].left = left_tree

        if left_tree is not None: self.nodes[left_tree].parent = p

    def __right_swap(self, v: int, p: int) -> None:
        right_tree = self.nodes[v].right; self.nodes[v].right = p
        self.nodes[p].parent = v;self.nodes[p].right = right_tree
        if right_tree is not None: self.nodes[right_tree].parent = p


n, _ = map(int,input().split()); tree = Tree(n)
swaps = list(map(int,input().split()))

for swp in swaps: tree.swap(swp)

tree.print()
