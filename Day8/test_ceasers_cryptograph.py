from ceasars_cryptograph import decoded_word, encoded_word


def test_decoded_word():
    assert decoded_word("qfufs", 1) == "peter"


def test_encoded_word():
    assert encoded_word("peter", 1) == "qfufs"


def test_encoded_shift_out_of_bound():
    assert encoded_word("_", 20) == "8"