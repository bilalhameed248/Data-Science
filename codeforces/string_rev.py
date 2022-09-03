from audioop import reverse


def str_rev(x):
    if len(x)==0:
        return x
    else:
        print(x[1:])
        return str_rev(x[1:])+x[0]

print(str_rev("Bilal Hameed"))