import numpy as np


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

#
# First Numpy-based network, page 35
#


weights = np.array([0.1, 0.2, 0])


def neural_network(inputs, weights):

    # applying dot product between inputs and weights
    return inputs.dot(weights)


def example_numpy_network_1():
    toes = np.array([8.5, 9.5, 9.9, 9.0])
    wlrec = np.array([0.65, 0.8, 0.8, 0.9])
    nfans = np.array([1.2, 1.3, 0.5, 1.0])

    inputs = np.array([toes[0], wlrec[0], nfans[0]])  # Inputs correspond to every entry for the first game
    pred = neural_network(inputs, weights)

    print(pred)

########################################################################

#
# Predicting with multiple inputs and outputs
#


# toes  % win  # fans
weights = [ [0.1,  0.1,   -0.3],  # hurt?
            [0.1,  0.2,    0.0],  # win?
            [0.0,  1.3,    0.1] ] # sad?


# Code page 43

# toes  % win  # fans
ih_wgt = np.array([
    [0.1,  0.2, -0.1],  # hid[0]
    [-0.1, 0.1,  0.9],  # hid[1]
    [0.1,  0.4,  0.1]   # hid[2]
]).T

# hid[0] hid[1] hid[2]
hp_wgt = np.array([
    [0.3, 1.1, -0.3],  # hurt?
    [0.1, 0.2,  0.0],  # win?
    [0.0, 1.3,  0.1]   # sad?
]).T

weights = [ih_wgt, hp_wgt]


def neural_network_multiple_outs(inputs, weights):

    hid = inputs.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred


if __name__ == '__main__':
    toes = np.array([8.5, 9.5, 9.9, 9.0])
    wlrec = np.array([0.65, 0.8, 0.8, 0.9])
    nfans = np.array([1.2, 1.3, 0.5, 1.0])
    input = np.array([toes[0], wlrec[0], nfans[0]])
    pred = neural_network_multiple_outs(input, weights)
    print(pred)
