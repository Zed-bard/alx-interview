Sure, here's how you can structure your `README.md` file for the Pascal's Triangle project:

```markdown
# Pascal's Triangle

This project provides a Python function `pascal_triangle(n)` that generates Pascal's Triangle up to the nth row and returns it as a list of lists of integers.

## Getting Started

To use this function, follow these steps:

### Prerequisites

Make sure you have Python 3 installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

### Installation

Clone this repository to your local machine using:

```bash
git clone https://github.com/Zed-bard/alx-interview.git
```

### Usage

1. Navigate to the `0x00-pascal_triangle` directory.
2. Import the `pascal_triangle` function in your Python script:

   ```python
   from 0-pascal_triangle import pascal_triangle
   ```

3. Use the function `pascal_triangle(n)` where `n` is the number of rows you want in the triangle. For example:

   ```python
   triangle = pascal_triangle(5)
   ```

   This will generate Pascal's Triangle up to the 5th row.

4. Print the triangle using the provided `print_triangle` function or customize your own output method.

## Example

```python
from 0-pascal_triangle import pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
```

Output:
```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

