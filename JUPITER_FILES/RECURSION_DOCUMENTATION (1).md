# Recursion in Python: Complete Guide

## Table of Contents
1. [Introduction to Recursion](#introduction)
2. [How Recursion Works](#how-recursion-works)
3. [Key Components](#key-components)
4. [Basic Examples](#basic-examples)
5. [Divide and Conquer Strategy](#divide-and-conquer)
6. [Recursion vs Iteration](#recursion-vs-iteration)
7. [Best Practices](#best-practices)
8. [Common Pitfalls](#common-pitfalls)

---

## Introduction to Recursion

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems. A recursive function solves a problem by solving smaller instances of the same problem until it reaches a base case that can be solved directly.

### When to Use Recursion
- Problems that have a recursive structure (e.g., tree traversal, factorial calculation)
- Divide-and-conquer problems
- Backtracking problems
- When the solution is naturally recursive in nature

---

## How Recursion Works

### The Recursion Call Stack

When a function calls itself, the call is added to the call stack. Each recursive call waits for the inner call to complete before continuing.

```
factorial(5)
  → factorial(4)
    → factorial(3)
      → factorial(2)
        → factorial(1)  [Base case reached]
        ← returns 1
    ← returns 2 * 1 = 2
  ← returns 3 * 2 = 6
← returns 4 * 6 = 24
← returns 5 * 24 = 120
```

### Memory Considerations

- Each function call uses stack memory
- Deep recursion can cause a **RecursionError** (stack overflow)
- Python has a default recursion limit of ~1000

---

## Key Components

### 1. Base Case
The condition that stops the recursion. Without it, the function would call itself infinitely.

```python
def factorial(n):
    if n == 0 or n == 1:  # ← Base case
        return 1
    return n * factorial(n - 1)
```

### 2. Recursive Case
The function calls itself with a smaller or simpler version of the problem.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # ← Recursive case
```

### 3. Progress Toward Base Case
Each recursive call must move closer to the base case, otherwise you'll have infinite recursion.

```python
def countdown(n):
    if n <= 0:            # Base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)  # Getting closer to base case
```

---

## Basic Examples

### Example 1: Factorial
Calculate n! = n × (n-1) × (n-2) × ... × 1

```python
def factorial(n):
    """
    Calculate factorial of n recursively.
    
    Args:
        n: Non-negative integer
    
    Returns:
        Factorial of n
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Examples
print(factorial(5))   # Output: 120
print(factorial(0))   # Output: 1
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) due to call stack

---

### Example 2: Fibonacci Sequence
Calculate the nth Fibonacci number: F(n) = F(n-1) + F(n-2)

```python
# Simple but inefficient approach
def fibonacci(n):
    """Calculate nth Fibonacci number (naive approach)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# More efficient approach with memoization
def fibonacci_memo(n, memo=None):
    """Calculate nth Fibonacci number with memoization."""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Examples
print(fibonacci(6))        # Output: 8 (but slow for large n)
print(fibonacci_memo(50))  # Output: 12586269025 (fast!)
```

**Naive Time Complexity:** O(2^n) - exponential, very slow!  
**With Memoization:** O(n) - much better!

---

### Example 3: Sum of List Elements

```python
def sum_list(numbers):
    """Calculate sum of all elements in a list recursively."""
    # Base case: empty list
    if len(numbers) == 0:
        return 0
    
    # Recursive case: first element + sum of rest
    return numbers[0] + sum_list(numbers[1:])

# Example
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
```

---

### Example 4: Binary Search
Search for a target value in a sorted array

```python
def binary_search(arr, target, left, right):
    """
    Search for target in sorted array using binary search.
    
    Args:
        arr: Sorted list
        target: Value to search for
        left: Left index
        right: Right index
    
    Returns:
        Index of target if found, -1 otherwise
    """
    if left > right:
        return -1  # Base case: not found
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid  # Base case: found
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)  # Search right
    else:
        return binary_search(arr, target, left, mid - 1)   # Search left

# Example
sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(sorted_arr, 7, 0, len(sorted_arr) - 1))  # Output: 3
print(binary_search(sorted_arr, 10, 0, len(sorted_arr) - 1)) # Output: -1
```

**Time Complexity:** O(log n)  
**Space Complexity:** O(log n) due to call stack depth

---

## Divide and Conquer Strategy

The divide-and-conquer approach breaks a problem into:
1. **Divide:** Split the problem into subproblems
2. **Conquer:** Solve subproblems recursively
3. **Combine:** Merge the solutions

### Example 1: Merge Sort

```python
def merge_sort(arr):
    """Sort array using merge sort (divide and conquer)."""
    if len(arr) <= 1:
        return arr  # Base case
    
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Combine
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
```

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

---

### Example 2: Quick Sort

```python
def quick_sort(arr):
    """Sort array using quick sort (divide and conquer)."""
    if len(arr) <= 1:
        return arr  # Base case
    
    # Choose pivot and partition
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
```

---

### Example 3: Binary Exponentiation

Calculate a^n efficiently using divide and conquer

```python
def power(base, exp):
    """Calculate base^exp using divide and conquer."""
    # Base case
    if exp == 0:
        return 1
    
    # If exponent is even
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    # If exponent is odd
    else:
        return base * power(base, exp - 1)

# Example
print(power(2, 10))  # Output: 1024
print(power(3, 5))   # Output: 243
```

**Time Complexity:** O(log n)  
**Space Complexity:** O(log n)

---

## Recursion vs Iteration

### Recursion Approach

```python
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

**Advantages:**
- More elegant and readable for recursive problems
- Natural fit for divide-and-conquer
- Easier to understand tree-like structures

**Disadvantages:**
- Higher memory usage (call stack)
- Risk of stack overflow for deep recursion
- Potentially slower due to function call overhead

---

### Iteration Approach

```python
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

**Advantages:**
- Lower memory consumption
- No stack overflow risk
- Generally faster execution

**Disadvantages:**
- Can be less elegant for recursive problems
- Requires explicit state management
- Less natural for some problem types

---

### Side-by-Side Comparison

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| **Memory** | O(n) stack | O(1) stack |
| **Speed** | Slower (overhead) | Faster |
| **Code Readability** | Often cleaner | Can be verbose |
| **Stack Overflow Risk** | High for deep calls | None |
| **Best For** | Divide-and-conquer | Simple loops |

---

## Best Practices

### 1. Always Define a Base Case
```python
def good_recursion(n):
    if n <= 0:  # ← Clear base case
        return 0
    return n + good_recursion(n - 1)
```

### 2. Ensure Progress Toward Base Case
```python
# Bad: infinite recursion
def bad_recursion(n):
    return bad_recursion(n)

# Good: progresses toward base case
def good_recursion(n):
    if n <= 0:
        return 0
    return n + good_recursion(n - 1)
```

### 3. Use Memoization for Overlapping Subproblems
```python
def fibonacci_optimal(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_optimal(n-1, memo) + fibonacci_optimal(n-2, memo)
    return memo[n]
```

### 4. Consider Recursion Limit
```python
import sys

# Check current limit
print(sys.getrecursionlimit())  # Usually 1000

# Increase if needed (be careful!)
sys.setrecursionlimit(5000)
```

### 5. Prefer Iteration for Deep Recursion
```python
# Bad: may exceed recursion limit
def deep_recursion_bad(n):
    if n == 0:
        return 0
    return deep_recursion_bad(n - 1)

# Better: use iteration
def deep_recursion_good(n):
    result = 0
    for i in range(n):
        result += i
    return result
```

---

## Common Pitfalls

### Pitfall 1: Missing Base Case
```python
# ❌ Infinite recursion!
def countdown(n):
    print(n)
    countdown(n - 1)

# ✅ Fixed with base case
def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 1)
```

### Pitfall 2: Inefficient Recursion
```python
# ❌ Exponential time complexity
def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)

# ✅ Use memoization
def fast_fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fast_fibonacci(n-1, memo) + fast_fibonacci(n-2, memo)
    return memo[n]
```

### Pitfall 3: Not Handling Edge Cases
```python
# ❌ Fails for negative numbers
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# ✅ Handle edge cases
def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### Pitfall 4: Stack Overflow
```python
# ❌ Can exceed recursion limit
def sum_recursive(nums):
    if not nums:
        return 0
    return nums[0] + sum_recursive(nums[1:])

# ✅ Use iteration for large inputs
def sum_iterative(nums):
    return sum(nums)
```

---

## Summary

| Concept | Key Points |
|---------|-----------|
| **Base Case** | Condition that stops recursion |
| **Recursive Case** | Function calls itself with simpler input |
| **Divide & Conquer** | Divide problem, solve subproblems, combine |
| **Memoization** | Cache results to avoid recomputation |
| **When to Use** | Tree traversal, sorting, searching, dynamic problems |
| **When to Avoid** | Deep recursion, simple loops, performance-critical code |

---

## Quick Reference

```python
# Template for recursive function
def recursive_function(n):
    # Base case: stop condition
    if base_case_condition:
        return base_case_value
    
    # Recursive case: call with simpler input
    return combine(recursive_function(simpler_input))
```
