from random import randint


def theKth_min(arr, k):
    if k > len(arr):
        exit(print("error input"))

    # a[p:q]上第i大的数
    def K(a, i, p, q):
        if p == q:
            return a[p]

        # 在[p:q]任取一点，返回该点应处于a（排序后）中的位置
        def partition(_a, _p, _q):
            r = randint(_p, _q)
            _a[r], _a[_p] = _a[_p], _a[r]
            pivot = _a[_p]
            m = _p
            n = _p + 1
            while n <= _q:
                if _a[n] <= pivot:
                    _a[m + 1], _a[n] = _a[n], _a[m + 1]
                    n += 1
                    m += 1
                else:
                    n += 1
            _a[_p], _a[m] = _a[m], _a[_p]
            return m

        rank = partition(a, p, q) + 1
        # 比较该值位置与所求位置的关系，等于则为所求值，小于则左搜索，大于则右搜索
        if i == rank:
            return a[rank - 1]
        elif i < rank:
            return K(a, i, p, rank - 2)
        else:
            return K(a, i, rank, q)

    return K(arr, k, 0, len(arr) - 1)


print(theKth_min([7, 5, 9, 2, 1, 655], 6))
