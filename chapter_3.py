
# Vector math challenge page 31.


def elementwise_multiplication(vec_a, vec_b):
    assert len(vec_a) == len(vec_b)
    return [vec_a[i] * vec_b[i] for i in range(0, len(vec_a))]


def elementwise_addition(vec_a, vec_b):
    assert len(vec_a) == len(vec_b)
    return [vec_a[i] + vec_b[i] for i in range(0, len(vec_a))]


def vector_sum(vec_a):
    ans = 0
    for i in vec_a:
        ans += i

    return ans


def vector_average(vec_a):
    return vector_sum(vec_a) / len(vec_a)


if __name__ == '__main__':
    print(elementwise_multiplication([1, 2, 3], [1, 2, 3]))
    print(elementwise_addition([1, 2, 3], [1, 2, 3]))
    print(vector_sum([1, 2, 3]))
    print(vector_average([3,3,3]))
