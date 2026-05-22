````markdown
# Financial Decision Tree Maximum Depth

## Assignment Overview

The purpose of this assignment was to determine the maximum depth of a binary decision tree used in a financial institution’s customer decision support system. The binary tree represents a sequence of Yes/No questions used to recommend financial products such as loans, mortgages, investments, and insurance.

The goal of the project was to calculate the longest path from the root question to the deepest final recommendation node. This helps measure the complexity of customer interactions and system performance.

This project was completed in Python.

---

# Files Included

- `decision_tree_depth.py`
- `test_decision_tree_depth.py`
- `README.md`
- `flowchart.md`

---

# Problem Description

A financial institution uses a binary decision tree to guide customer service representatives through customer consultations.

Each node in the tree represents:

- a financial question
- a Yes/No decision
- a final recommendation

The challenge is to determine the maximum depth of the tree, which represents the longest sequence of questions a customer may go through before receiving a recommendation.

---

# Clarifying Questions

Before solving the problem, these questions would be important to ask:

1. Should an empty tree have a depth of 0?
2. Should a tree with only a root node have a depth of 1?
3. Are all decisions strictly Yes/No?
4. Do final recommendations count as nodes in the depth?
5. Can the tree be unbalanced or skewed?

Assumptions used for this project:

- An empty tree has depth 0.
- A single root node has depth 1.
- Final recommendations count as leaf nodes.
- Trees may be balanced or skewed.

---

# Approach

The solution uses recursion to calculate the maximum depth.

For every node:

1. If the node is `None`, return 0.
2. Recursively calculate the depth of the Yes branch.
3. Recursively calculate the depth of the No branch.
4. Return 1 plus the larger depth.

Recursive formula:

```text
max_depth(root) = 1 + max(left_depth, right_depth)
```

---

# TreeNode Class

The program uses a `TreeNode` class to represent each question or recommendation in the financial decision tree.

Each node stores:

- the question or recommendation
- a Yes branch
- a No branch

Example:

```python
class TreeNode:
    def __init__(self, question):
        self.question = question
        self.yes = None
        self.no = None
```

---

# Maximum Depth Function

The `max_depth()` function calculates the maximum depth of the binary tree.

Example:

```python
def max_depth(root):
    if root is None:
        return 0

    yes_depth = max_depth(root.yes)
    no_depth = max_depth(root.no)

    return 1 + max(yes_depth, no_depth)
```

---

# Flowchart

```text
Start
  |
Check if current node is None
  |
  |-- Yes --> Return 0
  |
  |-- No
        |
Find depth of Yes branch
        |
Find depth of No branch
        |
Choose larger depth
        |
Add 1 for current node
        |
Return result
```

---

# Example Financial Decision Tree

```text
Does the customer need to borrow money?
├── Yes: Is the loan for a home?
│   ├── Yes: Recommend mortgage options
│   └── No: Recommend personal loan options
└── No: Does the customer want to invest money?
    ├── Yes: Recommend investment products
    └── No: Does the customer need insurance?
        ├── Yes: Recommend insurance products
        └── No: Recommend general financial consultation
```

Maximum Depth:

```text
4
```

---

# Test Cases and Results

## Test Case 1: Sample Financial Tree

Input:

```text
Financial decision tree with loans, investments, and insurance
```

Expected Output:

```text
4
```

Actual Output:

```text
4
```

Result:

```text
PASS
```

---

## Test Case 2: Tree With Only Root Node

Input:

```text
Single question node
```

Expected Output:

```text
1
```

Actual Output:

```text
1
```

Result:

```text
PASS
```

---

## Test Case 3: Balanced Tree

Input:

```text
Root node with one Yes child and one No child
```

Expected Output:

```text
2
```

Actual Output:

```text
2
```

Result:

```text
PASS
```

---

## Test Case 4: Empty Tree

Input:

```text
None
```

Expected Output:

```text
0
```

Actual Output:

```text
0
```

Result:

```text
PASS
```

---

## Test Case 5: Left-Skewed Tree

Input:

```text
Tree where every node only has a Yes branch
```

Expected Output:

```text
3
```

Actual Output:

```text
3
```

Result:

```text
PASS
```

---

## Test Case 6: Right-Skewed Tree

Input:

```text
Tree where every node only has a No branch
```

Expected Output:

```text
4
```

Actual Output:

```text
4
```

Result:

```text
PASS
```

---

# Program Output

```text
Financial Decision Tree Maximum Depth: 4
```

---

# Time Complexity

The algorithm visits every node exactly one time.

Time Complexity:

```text
O(n)
```

Where:

- `n` is the number of nodes in the tree.

---

# Space Complexity

The recursive call stack stores function calls while traversing the tree.

Space Complexity:

```text
O(h)
```

Where:

- `h` is the height of the tree.

Worst Case:

```text
O(n)
```

This occurs when the tree is completely skewed.

---

# Challenges Faced

One challenge was understanding how recursion moves through the tree and returns values back through the recursive calls. Another challenge was handling edge cases such as empty trees and skewed trees.

To solve these issues, I used a base case that returns 0 when the node is `None`. I also tested multiple tree structures to verify that the algorithm handled both balanced and unbalanced trees correctly.

Another challenge was making sure the recursive function counted the current node correctly while still choosing the deepest branch.

---

# Conclusion

This project successfully implemented a recursive algorithm to determine the maximum depth of a binary decision tree.

The solution correctly handled:

- normal trees
- balanced trees
- skewed trees
- empty trees
- single-node trees

The included unit tests verified the correctness of the implementation for both normal and edge cases.

This assignment improved my understanding of:

- recursion
- binary trees
- tree traversal concepts
- recursive time and space complexity

---

# How to Run the Program

Run the main program:

```bash
python3 decision_tree_depth.py
```

Run the unit tests:

```bash
python3 -m unittest test_decision_tree_depth.py
```

Expected test output:

```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```
````

