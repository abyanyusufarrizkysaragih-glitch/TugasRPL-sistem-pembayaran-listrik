def bayar(n, d, kwh):
    t = 0
    if d == 900:
        t = kwh * 1352
    elif d == 1300:
        t = kwh * 1444
    elif d == 2200:
        t = kwh * 1699

    if kwh > 100:
        t = t + (t * 0.05)

    if kwh < 20:
        t = t - 10000

    p = t * 0.05
    t = t + p

    print("Nama: " + n)
    print("Tagihan: " + str(t))
    return t

bayar("Andi", 1300, 120)
