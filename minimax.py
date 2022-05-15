def children(node):
    return (node.left, node.mid, node.right)

def outcome(node, maximizing=True):
    if node.is_terminal():
        return node.val

    goal = max if maximizing else min
    return goal([outcome(n, not maximizing) for n in children(node)])

def minimax(tree):
    return outcome(tree.root, maximizing=True)
