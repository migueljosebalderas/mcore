from mdecorator import duration


@duration
def test_duration():
    for i in range(10000):
        print(i)


@duration
def test_duration2(x, y, z):
    print(f"{x}-{y}-{z}")
    for i in range(10):
        print(i)


if __name__ == "__main__":
    test_duration()
    test_duration2(1, 2, 3)
