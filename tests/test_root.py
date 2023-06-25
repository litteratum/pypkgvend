from rootlib import root_func


def test_root_func():
    assert (
        root_func()
        == "root func uses lib func: Hello from mylib!. Core func result: I am the core"
    )
