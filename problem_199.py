"""199. Binary Tree Right Side View


Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    queue, ll = deque([root]), []
    while queue:
        rv = None
        for _ in range(len(queue)):
            rv = queue.popleft()
            if rv.left:
                queue.append(rv.left)
            if rv.right:
                queue.append(rv.right)
        ll.append(rv.val)
    return ll
