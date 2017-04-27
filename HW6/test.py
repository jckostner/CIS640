import impl


class Check:
    def isbst(self, node):

        if node:
            if node.left:
                assert node.left.key < node.key
                self.isbst(node.left)

            if node.right:
                assert node.right.key > node.key
                self.isbst(node.right)


checker = Check()
noder = impl.Node(6, None, None)
nodel = impl.Node(3, None, None)
node = impl.Node(5, nodel, noder)
checker.isbst(node)
