def draw_tree(levels):
    if levels < 1:
        return
    for i in range(1, levels + 1):
        print(" " * (levels - i) + "*" * (2 * i - 1))
    print(" " * (levels - 1) + "|")


try:
    num_trees = int(input("Enter the number of trees you want to draw: "))
    num_level = int(input("Enter the number of levels for Tree: "))
    for i in range(num_trees):
        draw_tree(num_level)
except ValueError:
    print("Please enter valid integers for the number of trees and levels.")