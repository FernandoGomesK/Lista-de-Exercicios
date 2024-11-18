dix1 = {"a": 1,
        "b": 2,
        "c": 3,
}

dix2 = {"d": 1,
        "b": 2,
        "e": 3,
}

dix3 = dix1.copy()
dix3.update(dix2)
print(dix1)
print(dix2)
print(dix3)
