def pathSum(self, root: TreeNode, target_sum: int) -> int:
    def dfs(node: TreeNode, sums: List[int]) -> int:
        if not node:
            return 0
        sums = [s + node.val for s in sums] + [node.val]
        ans = sums.count(target_sum)
        ans += dfs(node.left, sums) if node.left else 0
        ans += dfs(node.right, sums) if node.right else 0
        return ans

    return dfs(root, [])
