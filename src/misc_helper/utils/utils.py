def validateDim(v: int):
    if v <= 0 or v % 8 != 0:
        raise ValueError("dimension must > 0 and divisible by 8")