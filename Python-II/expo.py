def expo(base, exponent):
    expo.calls += 1 # Used to track recursive call count
    # Write you recursive expo function here
    p = exponent
    if p == 0:
        return 1

    if p%2 == 1:
        p = p - 1
        return base * expo(base, p)
    else:
        p = p/2
        return expo(base, p) ** 2


expo.calls = 0


def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()
