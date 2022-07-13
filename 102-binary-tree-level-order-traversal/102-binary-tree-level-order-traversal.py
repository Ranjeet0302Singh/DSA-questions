class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result: List[List[int]] = []
        lay = [root]
        while lay:
            lay_values = []
            next_lay = []
            
            for node in lay:
                lay_values.append(node.val)
                if node.left:
                    next_lay.append(node.left)
                if node.right:
                    next_lay.append(node.right)
            
            lay = next_lay
            result.append(lay_values)
        
        return result