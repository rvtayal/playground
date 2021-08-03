import matplotlib.pyplot as plt
import math
import numpy as np


# variables
ANGLE_DIVIDE = -math.pi / 18
ANGLE_MUL = math.pi / 9

def get_collatz_path(num):
    path = [num]
    cur = num
    while cur != 1:
        if cur % 2 == 0:
            cur /= 2
        else:
            cur = 3*cur + 1
        path += [int(cur)]
    return path


def collatz_path_to_graph_points(path):
    path = path[::-1]
    g_points = np.zeros((2,len(path)))
    prev = 1
    angle = 0
    dist = 1
    for i in range(1, len(path)):
        cur = path[i]

        if cur > prev:
            # divided by 2
            angle += ANGLE_DIVIDE
        else:
            # 3x+1
            angle += ANGLE_MUL
        delta = np.array([dist * math.cos(angle), dist * math.sin(angle)]).reshape(2,)

        g_points[:, i] = g_points[:, i-1] + delta
        prev = cur
        dist *= 0.99

    ret_points = np.zeros((2,2, len(path)-1))
    for i in range(len(path)-1):
        ret_points[:,:, i] = g_points[:, [i, i+1]]
    return ret_points


def aggregate_points(nums):
    path = get_collatz_path(nums[0])
    points = collatz_path_to_graph_points(path)
    for num in nums[1:]:
        path = get_collatz_path(num)
        points = np.concatenate((points, collatz_path_to_graph_points(path)), axis=2)
    return points


def plot_points(points):
    fig, ax = plt.subplots()
    for i in range(points.shape[-1]):
        ax.plot(points[0,:, i], points[1,:, i], 'k')
    ax.axis('equal')
    return ax


def build_collatz_graph(nums):
    points = aggregate_points(nums)
    return plot_points(points)


if __name__ == "__main__":
    # nums = [2,4,17]
    nums = list(range(2,10))
    points = aggregate_points(nums)
    f = plot_points(points)
    plt.savefig('results/collatz_tree.png')
