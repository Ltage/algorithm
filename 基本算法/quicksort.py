def quick_sort(array: list) -> list:
    import random

    def partition(arr, left, right):
        if left >= right:
            return
        # 取随机数作为pivot
        random_idx = random.randint(left, right)
        arr[left], arr[random_idx] = arr[random_idx], arr[left]
        pivot = arr[left]
        # 设定快慢指针
        i = left
        j = left + 1
        while j <= right:
            if arr[j] <= pivot:
                arr[i + 1], arr[j] = arr[j], arr[i + 1]
                i += 1
                j += 1
            else:
                j += 1
        # pivot与慢指针指向的值做交换
        arr[i], arr[left] = arr[left], arr[i]
        partition(arr, left, i - 1)
        partition(arr, i + 1, right)

    partition(array, 0, len(array) - 1)
    return array
