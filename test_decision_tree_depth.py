import unittest
from decision_tree_depth import TreeNode, max_depth, build_sample_tree


class TestDecisionTreeDepth(unittest.TestCase):

    def test_sample_financial_tree(self):
        root = build_sample_tree()
        self.assertEqual(max_depth(root), 4)

    def test_tree_with_only_root(self):
        root = TreeNode("Start question")
        self.assertEqual(max_depth(root), 1)

    def test_balanced_tree(self):
        root = TreeNode("Root")
        root.yes = TreeNode("Yes question")
        root.no = TreeNode("No question")
        self.assertEqual(max_depth(root), 2)

    def test_empty_tree(self):
        self.assertEqual(max_depth(None), 0)

    def test_left_skewed_tree(self):
        root = TreeNode("Question 1")
        root.yes = TreeNode("Question 2")
        root.yes.yes = TreeNode("Question 3")
        self.assertEqual(max_depth(root), 3)

    def test_right_skewed_tree(self):
        root = TreeNode("Question 1")
        root.no = TreeNode("Question 2")
        root.no.no = TreeNode("Question 3")
        root.no.no.no = TreeNode("Question 4")
        self.assertEqual(max_depth(root), 4)


if __name__ == "__main__":
    unittest.main()
