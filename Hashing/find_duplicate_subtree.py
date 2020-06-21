from collections import defaultdict
class SameTree:
    def findDuplicateSuntrees(self,root: TreeNode) -> List[TreeNode]:
        count = defaultdict(int)
        ans = []
        def collect(node: TreeNode) -> str:
            if not node:
                return '#'
            serial = "{},{},{}".format(node.val,collect(node.left),collect(node.right))
            count[serial] += 1

            if count[serial] == 2:
                ans.append(node)
            
            return serial
        collect(root)
        return ans
