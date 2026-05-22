"""
File: decision_tree_depth.py
Author: Keona Truitt
Course: AD 325

Description:
This program finds the maximum depth of a binary decision tree.
The tree represents a financial institution's decision support system.
Each node is a question or final product recommendation.
"""


class TreeNode:
    def __init__(self, question):
        self.question = question
        self.yes = None
        self.no = None


def max_depth(root):
    if root is None:
        return 0

    yes_depth = max_depth(root.yes)
    no_depth = max_depth(root.no)

    return 1 + max(yes_depth, no_depth)


def build_sample_tree():
    root = TreeNode("Does the customer need to borrow money?")

    root.yes = TreeNode("Is the loan for a home?")
    root.no = TreeNode("Does the customer want to invest money?")

    root.yes.yes = TreeNode("Recommend mortgage options")
    root.yes.no = TreeNode("Recommend personal loan options")

    root.no.yes = TreeNode("Recommend investment products")
    root.no.no = TreeNode("Does the customer need insurance?")

    root.no.no.yes = TreeNode("Recommend insurance products")
    root.no.no.no = TreeNode("Recommend general financial consultation")

    return root


def main():
    decision_tree = build_sample_tree()
    depth = max_depth(decision_tree)

    print("Financial Decision Tree Maximum Depth:", depth)


if __name__ == "__main__":
    main()
