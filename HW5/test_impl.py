import pytest
from impl import Queue
import hypothesis.strategies as st
from hypothesis import given


class TestQueue:

    list_strat = st.lists(elements=(st.floats(allow_nan=False, allow_infinity=False) | st.text() | st.integers() |
                                    st.booleans() | st.dictionaries(st.integers(), st.integers())
                                    | st.lists(st.integers())))
    single_strat = st.one_of(st.floats(allow_infinity=False, allow_nan=False) | st.text() | st.integers() |
                             st.booleans() | st.dictionaries(st.integers(), st.integers()) |
                             st.lists(st.integers()))
    fail_single_strat = st.sampled_from([None, float('nan'), float('inf'), float('-inf')])

    # P1: Calls to enqueue that are successful should increment len by 1.
    @given(single_strat)
    def test_enqueue_p1(self, v):
        q = Queue()
        start_len = q.len()
        q.enqueue(v)
        assert start_len + 1 == q.len()

    # P2: Calls to enqueue that are unsuccessful should not affect the queue i.e. length should not increment.
    @given(fail_single_strat)
    def test_enqueue_p2(self, v):
        q = Queue()
        start_len = q.len()
        with pytest.raises(ValueError):
            q.enqueue(v)
        assert q.len() == start_len

    # P3: Calls to dequeue that are successful (non-None) should decrement len by 1 for non-empty queues.
    @given(list_strat)
    def test_dequeue_p3(self, v):
        q = Queue()
        for x in v:
            q.enqueue(x)
        start_len = q.len()
        item = q.dequeue()
        if item is None:
            pass
        else:
            assert start_len - 1 == q.len()

    # P4: Lens minimum value should be 0 i.e. calling decrement on an empty queue should not decrement len.
    def test_dequeue_p4(self):
        q = Queue()
        q.dequeue()
        assert q.len() == 0

    # P5: The initial value for len should be 0.
    def test_len_p5(self):
        q = Queue()
        assert q.len() == 0

    # P6: Enqueue should store values in the order they were placed, and dequeue should remove values in the same order,
    # meaning if you enqueue a number of objects and then immediately dequeue the same number of objects they should be
    # in the same order.
    @given(list_strat)
    def test_enqueue_dequeue_p6(self, v):
        q = Queue()
        initial_list = v
        for x in v:
            q.enqueue(x)
        return_list = []
        for x in v:
            return_list.append(q.dequeue())
        assert initial_list == return_list

    # P7: If you dequeue an empty Queue, it should return None.
    def test_dequeue_p7(self):
        q = Queue()
        assert q.dequeue() is None

    # P8: If you try to enqueue None, Inf, -Inf, or NaN, it should raise a ValueError.
    @given(fail_single_strat)
    def test_enqueue_p8(self, v):
        q = Queue()
        with pytest.raises(ValueError):
            q.enqueue(v)
            assert False
        assert True

    # P9: Calling len should not affect the order of the Queue.
    @given(list_strat)
    def test_len_p9(self, v):
        q = Queue()
        start_list = v
        for x in v:
            q.enqueue(x)
        q.len()
        end_list = []
        for x in v:
            end_list.append(q.dequeue())
        assert start_list == end_list

    # P10: When trying to enqueue a value that raises a ValueError, the order does not change
    @given(v=list_strat, w=fail_single_strat)
    def test_len_p10(self, v, w):
        q = Queue()
        start_list = v
        for x in v:
            q.enqueue(x)
        with pytest.raises(ValueError):
            q.enqueue(w)
        end_list = []
        for x in v:
            end_list.append(q.dequeue())
        assert end_list == start_list

