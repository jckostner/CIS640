import pytest
from impl import tic_tac_toe_check


class TestTicTacToeCheck:

    @pytest.mark.parametrize("board", ["string", "", None, 1, 1.12, True, (), {}])
    def test_tic_tac_toe_check_only_accepts_lists(self, board):
        with pytest.raises(TypeError, message="Method is supposed to raise TypeError on non-list inputs"):
            tic_tac_toe_check(board)

    @pytest.mark.parametrize("board", [[1.2, "x", "o", "o", "x", "o", "x", "o", "o"], [1, 2, 3, 4, 5, 6, 7, "x", "x"],
                                       [True, False, True, True, "o", "x", "o", "x", "x"],
                                       [None, "x", "o", "o", "x", "o", "x", "o", "o"], [[]], [()]])
    def test_tic_tac_toe_check_doesnt_accept_non_string_boards(self, board):
        with pytest.raises(TypeError, message=
                           "Method is supposed to raise TypeError on lists not containing all strings"):
            tic_tac_toe_check(board)

    @pytest.mark.parametrize("board", [["x", "o", "o", "x", "o", "x", "o", "o"],
                                       ["x", "o", "o", "x", "o", "x", "o", "o", "x", "x", "o"]])
    def test_tic_tac_toe_check_only_accepts_correct_board_size_lists(self, board):
        with pytest.raises(ValueError, message="Method is supposed to raise ValueError on incorrectly sized lists."):
            tic_tac_toe_check(board)

    def test_tic_tac_toe_check_only_accepts_lists_with_lowercase_x_or_o_or_empty(self):
        with pytest.raises(ValueError, message="Method is supposed to raise ValueError on lists not"
                                               " containing all 'x's, 'o's, and/or ''."):
            tic_tac_toe_check(["x", "o", "o", "x", "o", "x", "1", "z", "y"])

    def test_tic_tac_toe_check_returns_none_on_list_of_empties(self):
        value = tic_tac_toe_check(["", "", "", "", "", "", "", "", ""])
        assert value is None

    @pytest.mark.parametrize("board", [["x", "x", "x", "", "", "", "", "", ""], ["o", "x", "o", "x", "x", "o", "o", "x", "x"]])
    def test_tic_tac_toe_check_returns_x_as_winner(self, board):
        winner = tic_tac_toe_check(board)
        assert winner == 'x'

    @pytest.mark.parametrize("board", [["", "", "", "o", "o", "o", "", "", ""], ["x", "o", "x", "o", "o", "x", "x", "o", "o"]])
    def test_tic_tac_toe_check_returns_o_as_winner(self, board):
        winner = tic_tac_toe_check(board)
        assert winner == 'o'

    def test_tic_tac_toe_check_doesnt_return_empty_string_as_winner(self):
        winner = tic_tac_toe_check(["x", "o", "x", "", "", "", "x", "o", "x"])
        assert winner != ""

    @pytest.mark.parametrize("board", [["x", "x", "x", "x", "x", "x", "", "", ""], ["o", "o", "o", "o", "o", "o", "", "", ""], ["x", "x", "x", "o", "o", "o", "", "", ""]])
    def test_tic_tac_toe_check_raises_value_error_on_multiple_winning_patterns(self, board):
        with pytest.raises(ValueError, message="Method is supposed to raise ValueError on multiple winners."):
            tic_tac_toe_check(board)

    def test_tic_tac_toe_check_returns_none_on_no_winners(self):
        winner = tic_tac_toe_check(["x", "o", "x", "x", "x", "o", "o", "x", "o"])
        assert winner is None

    @pytest.mark.parametrize("board", [["x", "x", "x", "", "", "", "", "", ""], ["", "", "", "x", "x", "x", "", "", ""],
                                       ["", "", "", "", "", "", "x", "x", "x"], ["x", "", "", "", "x", "", "", "", "x"],
                                       ["", "", "x", "", "x", "", "x", "", ""], ["x", "", "", "x", "", "", "x", "", ""],
                                       ["", "x", "", "", "x", "", "", "x", ""], ["", "", "x", "", "", "x", "", "", "x"]])
    def test_tic_tac_toe_check_accepts_all_winning_pattern_types(self, board):
        winner = tic_tac_toe_check(board)
        assert winner == 'x'
