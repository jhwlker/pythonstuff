from pythonstuff import pythonstuff


def test_pythonstuff_main():
    expected = 'This is just to initialize the project. I\ll kill it later'

    actual = pythonstuff.pythonstuff_main()

    assert actual == expected
