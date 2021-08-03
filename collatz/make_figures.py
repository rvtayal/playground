import collatz
import matplotlib.pyplot as plt

# first 10 numbers
nums = list(range(2,10))
points = collatz.aggregate_points(nums)
f = collatz.plot_points(points)
plt.savefig('results/collatz_tree_10.png')