"""
Write a function that takes as arguments: an array of distinct integers and an
integer (target value).
You need to check if any two numbers of the array sum up to the target value.
If that's the case, your function should return those two numbers in array
fashion. Otherwise, just return an empty array.
"""


def two_sum(array, target):
    result_array = []
    for pos, value in enumerate(array):
        tamanho = len(array)
        for x in range(tamanho):
            if pos != x and x >= pos:
                if target == value + array[x]:
                    result_array.append(value)
                    result_array.append(array[x])
    return result_array


if __name__ == "__main__":
    array_one = [3, 5, -4, 8, 11, 1, -1, 6]
    array_two = [3, 5, 2, 8, 11, 1, -1, 6]
    array_three = [3, 4, 6, 8, 11, -1, 2, 7]
    target = 10

    print(two_sum(array_one, target))
    print(two_sum(array_two, target))
    print(two_sum(array_three, target))
