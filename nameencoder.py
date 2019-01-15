def encode(num):
    return "{}+{}".format(len(str(num)), num)


def decode(str_):
    return int(str_.rsplit('+')[-1])


a = 12334567890129876
print(encode(a), decode(encode(a)))
