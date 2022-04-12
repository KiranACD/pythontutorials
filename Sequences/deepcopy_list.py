
def deepcopy(a, mapping = dict()):

    copy_a = []
    mapping[id(a)] = copy_a

    if len(a) == 0:
        return copy_a

    n = len(a)

    for i in range(n):
        if id(a[i]) in mapping:
            copy_a.append(mapping[id(a[i])])
            continue
        if isinstance(a[i], list):
            copy_a.append(deepcopy(a[i], mapping))
        else:
            x = a[i]
            copy_a.append(x)
            mapping[id(a[i])] = x

    return copy_a