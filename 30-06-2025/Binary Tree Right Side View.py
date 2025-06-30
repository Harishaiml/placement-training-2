def rightSideView(root):
    if not root:
        return []
    queue, res = [root], []
    while queue:
        level_len = len(queue)
        for i in range(level_len):
            node = queue.pop(0)
            if i == level_len - 1:
                res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return res
