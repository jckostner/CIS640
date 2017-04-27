import impl
import pytest
import hypothesis.strategies as st
from hypothesis import given


class TestBST:

    single_strat = st.one_of(st.floats(allow_infinity=False, allow_nan=False) | st.integers())
    list_strat = st.lists(elements=(st.floats(allow_nan=False, allow_infinity=False) | st.integers()),
                          min_size=2, unique=True)

    # P1: Node method make_copy should return a node with the same key, left, and right values.
    @given(single_strat)
    def test_make_copy_p1(self, k):
        node = impl.Node(k, None, None)
        copy_node = impl.Node.make_copy(node)
        assert copy_node.key == node.key
        assert copy_node.left == node.left
        assert copy_node.right == node.right

    # P2: BST method search should return true if value is in the node or its children
    @given(list_strat)
    def test_search_p2(self, vs):
        bst = impl.BST()
        for x in vs:
            bst.insert(x)

        assert bst.search(vs[0])

    # P3: BST method search should return false if value in not in the node or its children
    @given(list_strat)
    def test_search_p3(self, vs):
        bst = impl.BST()
        count = 0
        for x in vs:
            if count != 0:
                bst.insert(x)
            count += 1

        assert not bst.search(vs[0])

    # P4: BST method insert should insert the value in correctly i.e. after successful insertion (insert returns true),
    # any node left of a certain node should be less than that node and any node right of a certain node should be
    # greater than that node.
    @given(list_strat)
    def test_insert_p4(self, vs):
        bst = impl.BST()
        for x in vs:
            assert bst.insert(x)

        self.isbst(bst.root)

    # P5: BST method insert should not affect the BST if it fails to insert i.e. after a failed insertion (insert
    # returns false via attempt to add a duplicate Node) the BST should be valid, as given by P8.
    @given(list_strat)
    def test_insert_p5(self, vs):
        bst = impl.BST()
        for x in vs:
            bst.insert(x)

        assert not bst.insert(vs[0])
        self.isbst(bst.root)

    # P6: BST method delete should leave the BST in correct order i.e. after a successful deletion (delete returns
    # true), all nodes left of a certain node are less than the node and all nodes right of a node are greater than the
    # node.
    @given(vs=list_strat, r=st.randoms())
    def test_delete_p6(self, vs, r):
        bst = impl.BST()
        for x in vs:
            bst.insert(x)

        assert bst.delete(r.choice(vs))
        self.isbst(bst.root)

    # P7: BST method delete shouldn't affect the BST if the value was not present i.e. when delete returns false the
    # BST should be equal to what it was immediately before the call.
    @given(list_strat)
    def test_delete_p7(self, vs):
        bst = impl.BST()
        count = 0
        for x in vs:
            if count != 0:
                bst.insert(x)
            count += 1
        current_bst = bst
        assert not bst.delete(vs[0])
        self.isbst(bst.root)
        assert current_bst == bst

    # P8: BST method delete should delete the Node containing the value, as in searching for the value immediately
    # after a delete call on that value should cause delete to return false.
    @given(vs=list_strat, r=st.randoms())
    def test_delete_search_p8(self, vs, r):
        bst = impl.BST()
        for x in vs:
            bst.insert(x)

        i = r.choice(vs)
        assert bst.delete(i)
        assert not bst.search(i)

    # P9: BST method root should return none if no nodes have been added to the BST.
    def test_root_p9(self):
        bst = impl.BST()
        assert not bst.root

    # P10: BST method search should not affect the BST i.e. the BST should be equal right before a search call and right
    # after the search call
    @given(vs=list_strat, r=st.randoms())
    def test_search_p10(self, vs, r):
        bst = impl.BST()
        for x in vs:
            bst.insert(x)

        init_bst = bst
        bst.search(r.choice(vs))
        assert bst == init_bst

    def isbst(self, node):

        if node:
            if node.left:
                assert node.left.key < node.key
                self.isbst(node.left)

            if node.right:
                assert node.right.key > node.key
                self.isbst(node.right)
