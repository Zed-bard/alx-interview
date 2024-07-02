
# Lockboxes

## Overview

This project involves developing an algorithm in Python to determine if all boxes can be opened given a series of locked boxes and keys. Each box is numbered sequentially from 0 to n - 1 and may contain keys to other boxes. The goal is to figure out if you can unlock all the boxes starting from the first box (which is initially unlocked).

## Project Details

- **Weight**: 1
- **Start Date**: Jun 30, 2024, 11:00 PM
- **End Date**: Jul 4, 2024, 11:00 PM
- **Checker Release Date**: Jul 1, 2024, 11:00 PM
- **Auto Review**: Launched at the deadline

## Must Know Concepts

To develop a solution for this project, a solid understanding of the following concepts is necessary:

### Lists and List Manipulation

- **Concept**: Accessing elements, iterating over lists, and modifying lists dynamically.
- **Resource**: [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

### Graph Theory Basics

- **Concept**: Traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS) can be useful.
- **Resource**: [Graph Theory (Khan Academy)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:graph-theory)

### Algorithmic Complexity

- **Concept**: Understanding time and space complexity to write efficient algorithms.
- **Resource**: [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

### Recursion

- **Concept**: Using recursion to traverse through boxes and keys.
- **Resource**: [Recursion in Python (Real Python)](https://realpython.com/python-thinking-recursively/)

### Queue and Stack

- **Concept**: Implementing BFS or DFS using queues and stacks.
- **Resource**: [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

### Set Operations

- **Concept**: Using sets for tracking visited boxes and available keys.
- **Resource**: [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Additional Resources

- **Mock Technical Interview**

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should be documented
- Code should follow PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks

### 0. Lockboxes

**Mandatory**

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- **Prototype**: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- Assume all keys are positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

**Example**

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

**Repository**

- **GitHub repository**: `alx-interview`
- **Directory**: `0x01-lockboxes`
- **File**: `0-lockboxes.py`
