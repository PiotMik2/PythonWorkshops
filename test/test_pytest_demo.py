import pytest

def test_simple_assertion():
    assert True

def test_simple_comparison():
    assert 4 == 2 + 2


@pytest.mark.parametrize(
    "expected, inputs",
    [
        (5,  [2, 3]), 
        (-1, [4, -5]), 
        (5,  [5]), 
        (10, [2, 3, 4, 1])
    ],
    ids=[
        "All positive",
        "One negative",
        "One arg",
        "Multiple args"
    ]
)
def test_parameterized(expected, inputs):
    actual_result = sum(inputs)
    assert expected == actual_result


def test_expected_failure():
    with pytest.raises(ZeroDivisionError):
        5.0 / 0.0

if __name__ == "__main__":
    pass
