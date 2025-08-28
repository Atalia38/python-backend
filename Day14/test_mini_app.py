# test_mini_app.py
import pytest
import mini_app


# --- greet() ---
@pytest.mark.parametrize(
    "raw,expected",
    [
        ("alice", "Hello, Alice!"),
        ("  bob   marley ", "Hello, Bob Marley!"),
        ("", "Hello, World!"),
    ],
)
def test_greet_happy(raw, expected):
    assert mini_app.greet(raw) == expected


def test_greet_type_error():
    with pytest.raises(TypeError):
        mini_app.greet(123)  # type: ignore[arg-type]


# --- fibonacci() ---
@pytest.mark.parametrize(
    "n,expected",
    [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55)],
)
def test_fibonacci_values(n, expected):
    assert mini_app.fibonacci(n) == expected


def test_fibonacci_errors():
    with pytest.raises(ValueError):
        mini_app.fibonacci(-1)
    with pytest.raises(TypeError):
        mini_app.fibonacci(3.14)  # type: ignore[arg-type]


# --- Counter class (with mocking via pytest-mock) ---
def test_counter_inc_dec_and_callback(mocker):
    cb = mocker.Mock()
    c = mini_app.Counter(on_change=cb)

    c.inc()
    c.inc(2)
    c.dec()

    assert c.value == 2
    cb.assert_has_calls([mocker.call(1), mocker.call(3), mocker.call(2)])


def test_counter_invalid_steps():
    c = mini_app.Counter()
    for fn in (c.inc, c.dec):
        with pytest.raises(ValueError):
            fn(0)
        with pytest.raises(ValueError):
            fn(-5)
