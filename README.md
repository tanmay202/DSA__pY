# DSA__pY: Data Structures & Algorithms in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

A comprehensive collection of Data Structures and Algorithms problems solved in Python with detailed explanations, optimizations, and complexity analysis.

[🔗 Quick Navigation](#quick-navigation) • [📚 Topics](#topics-by-data-structure) • [🎯 Problems](#problem-index) • [💡 Contribute](#contributing)

</div>

---

## 📖 About This Repository

This repository is a structured learning resource for mastering Data Structures and Algorithms through Python. Each problem includes:
- ✅ Multiple solution approaches
- 📊 Time & Space complexity analysis
- 🔍 Detailed explanations
- 🧪 Test cases and edge cases
- 💻 Runnable Jupyter notebooks

**Target Audience:** Students, developers preparing for technical interviews, and anyone looking to strengthen their DSA fundamentals.

---

## 🚀 Quick Navigation

### Jump to Topics
| Topic | Difficulty | Count | View |
|-------|------------|-------|------|
| [**Arrays**](#arrays) | Beginner to Intermediate | 15+ | [Explore →](#arrays) |
| [**Linked Lists**](#linked-lists) | Intermediate | — | Coming Soon |
| [**Stacks & Queues**](#stacks--queues) | Intermediate | — | Coming Soon |
| [**Trees**](#trees) | Intermediate to Advanced | — | Coming Soon |
| [**Graphs**](#graphs) | Advanced | — | Coming Soon |
| [**Dynamic Programming**](#dynamic-programming) | Advanced | — | Coming Soon |

---

## 📚 Topics by Data Structure

### Arrays

The foundation of data structures. Master array manipulation, searching, sorting, and optimization techniques.

#### Phase 0: Absolute Basics
<details>
<summary><b>📖 Fundamentals & Core Concepts</b></summary>

- **[Array Fundamentals](ARRAY/Phase%200%20—%20Absolute%20Basics/ArrayFundamental.ipynb)**

</details>

#### Phase 0:Basic Array Problems
<details>
<summary><b>🎯 Basic Array Problems & Solutions</b></summary>

  - Problem 1: [Move zeros to end](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/1.Move%20zeroes%20to%20end.py)
  - Problem 2: [RotatingArray](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/2.RotatingArray.py)
  - Problem 3: [Find Frequency](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/3.Find_frequency.py)
  - Problem 4: [Find Duplicates](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/4.Find_duplicate.py)
  - Problem 5: [Find missing numbers](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/5.Find_Missing_Number.py)
  - Problem 6: [Contain duplicate or not](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/6.ContainDuplicateOrNot.py)
  - Problem 7: [Binary Search](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/7.BinarySearch.py)
  - Problem 8: Move zeros to end
  - And more...

</details>

---

## 🎯 Problem Index

### By Difficulty Level

#### 🟢 Easy (Beginner)
| # | Problem | Topic | Concepts | Solution |
|---|---------|-------|----------|----------|
| 1 | Find Maximum Element | Arrays | Iteration, Comparison | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |
| 2 | Reverse an Array | Arrays | In-place modification, Two pointers | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |
| 3 | Check if Array is Sorted | Arrays | Iteration, Logical conditions | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |
| 4 | Second Largest Element | Arrays | Sorting, Comparison | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |
| 5 | Linear Search | Arrays | Sequential search | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |

#### 🟡 Medium (Intermediate)
| # | Problem | Topic | Concepts | Solution |
|---|---------|-------|----------|----------|
| 6 | Duplicate Elements | Arrays | HashSet, Hashing | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |
| 7 | Move Zeros to End | Arrays | Two pointers, In-place | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |
| 8 | Array Rotation | Arrays | Index manipulation, Rotation | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |
| 9 | Remove Duplicates | Arrays | HashSet, Two pointers | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |
| 10 | Merge Sorted Arrays | Arrays | Sorting, Merging | [View](ARRAY/Phase%200%20—%20Absolute%20Basics/Problems/Basic_Array_Problems_Python_DSA.ipynb) |

#### 🔴 Hard (Advanced)
| # | Problem | Topic | Concepts | Solution |
|---|---------|-------|----------|----------|
| 11+ | Advanced Array Problems | Arrays | Dynamic Programming, Optimization | Coming Soon |

### By Topic/Concept

#### Searching & Sorting
- Linear Search
- Binary Search (Coming Soon)
- Bubble Sort
- Quick Sort
- Merge Sort

#### Array Manipulation
- Array Rotation
- Array Reversal
- Duplicate Removal
- Zero Movement
- Element Shifting

#### Two-Pointer Techniques
- Reverse Array
- Move Zeros
- Container with Most Water (Coming Soon)
- Valid Palindrome (Coming Soon)

---

## 📊 Complexity Reference

### Time Complexity Cheatsheet
```
O(1)     - Constant time (Direct access, arithmetic operations)
O(log n) - Logarithmic (Binary Search, Balanced trees)
O(n)     - Linear (Simple loops, linear search)
O(n²)    - Quadratic (Nested loops, bubble sort)
O(2ⁿ)    - Exponential (Recursive problems without optimization)
O(n!)    - Factorial (Permutations)
```

### Space Complexity Notes
- **In-place:** O(1) space (modify input directly)
- **Auxiliary:** O(n) space (extra data structure needed)

---

## 🛠️ Setup & Usage

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook/Lab
- Basic understanding of Python

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/DSA__pY.git
cd DSA__pY

# Install dependencies (optional)
pip install jupyter notebook numpy pandas matplotlib

# Launch Jupyter
jupyter notebook
```

### How to Use

1. **Browse by Topic:** Start with the topic that interests you
2. **Read the Fundamentals:** Begin with phase 0 basics for each data structure
3. **Solve Problems:** Practice the problems in order of difficulty
4. **Analyze Solutions:** Study the optimized solutions and complexity analysis
5. **Experiment:** Modify code and test with your own test cases

---

## 📖 Learning Path Recommendation

### For Beginners
1. Start with **Phase 0: Array Fundamentals**
2. Solve **Easy Problems** (Easy difficulty level)
3. Understand basic concepts before moving to intermediate

### For Interview Preparation
1. Review all phases and problem types
2. Focus on **Medium and Hard problems**
3. Practice **Optimal solutions** with best time/space complexity
4. Solve problems without looking at solutions first

### For Competitive Programming
1. Master all data structures
2. Focus on **Advanced/Hard problems**
3. Optimize for time complexity
4. Practice speed and accuracy

---

## 📁 Repository Structure

```
DSA__pY/
├── README.md                          # This file
├── ARRAY/                             # Arrays data structure
│   ├── Phase 0 — Absolute Basics/
│   │   ├── ArrayFundamental.ipynb    # Concepts & fundamentals
│   │   └── Problems/
│   │       └── Basic_Array_Problems_Python_DSA.ipynb
│   ├── Phase 1 — Intermediate/       # (Coming Soon)
│   └── Phase 2 — Advanced/           # (Coming Soon)
├── LINKED_LISTS/                     # (Coming Soon)
├── STACKS_QUEUES/                    # (Coming Soon)
├── TREES/                            # (Coming Soon)
├── GRAPHS/                           # (Coming Soon)
└── DYNAMIC_PROGRAMMING/              # (Coming Soon)
```

---

## 🏆 Topics Roadmap

- [x] Arrays - Phase 0 (Absolute Basics)
- [ ] Arrays - Phase 1 (Intermediate)
- [ ] Arrays - Phase 2 (Advanced)
- [ ] Linked Lists - Complete
- [ ] Stacks & Queues - Complete
- [ ] Trees - Complete
- [ ] Graphs - Complete
- [ ] Dynamic Programming - Complete
- [ ] Sorting Algorithms - Complete
- [ ] Searching Algorithms - Complete

---

## 💡 Key Features

✨ **What Makes This Repository Special:**

- 📚 **Comprehensive Coverage:** From basics to advanced DSA topics
- 🎓 **Multiple Approaches:** Each problem shows multiple solutions
- ⚡ **Complexity Analysis:** Detailed time & space complexity for every solution
- 🔍 **Visual Explanations:** Step-by-step walkthroughs with examples
- 🧪 **Test Cases:** Edge cases and comprehensive testing
- 📝 **Interactive Notebooks:** Jupyter notebooks for hands-on learning
- 🎯 **Problem Index:** Quick navigation by difficulty, topic, and concept

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### How to Contribute

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/new-problem`
3. **Add** your solution with proper documentation
4. **Ensure** your code includes:
   - Problem statement
   - Solution approach with explanation
   - Time & space complexity analysis
   - Multiple test cases
   - Edge case handling
5. **Submit** a Pull Request with a clear description

### Contribution Guidelines

- Follow PEP 8 Python style guide
- Include docstrings for all functions
- Add complexity analysis for all solutions
- Test your code thoroughly
- Update the README if adding new topics/problems

---

## 📚 Resources & References

### Learning Materials
- [LeetCode](https://leetcode.com/) - Practice platform
- [GeeksforGeeks DSA](https://www.geeksforgeeks.org/data-structures/) - Tutorials
- [Cracking the Coding Interview](https://www.crackingthecodinginterview.com/) - Book
- [Python Official Docs](https://docs.python.org/3/) - Reference

### Useful Tools
- [Python Tutor](https://pythontutor.com/) - Visualize code execution
- [Complexity Cheatsheet](https://www.bigocheatsheet.com/) - Big O reference
- [Jupyter Notebook](https://jupyter.org/) - Interactive coding

---

## 📞 Contact & Support

Have questions or suggestions? Feel free to:
- **Open an Issue** for bugs or feature requests
- **Submit a Pull Request** with improvements
- **Discuss** in the Discussions tab

---

## 📄 License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Show Your Support

If this repository helped you in your learning journey, please consider:
- ⭐ Starring the repository
- 🔖 Bookmarking for future reference
- 👥 Sharing with your friends/colleagues
- 💬 Providing feedback and suggestions

---

## 🎯 Next Steps

1. **Star this repository** ⭐
2. **Clone and explore** the code
3. **Start with Phase 0 Basics**
4. **Solve problems** at your own pace
5. **Share your learnings** with others

---

<div align="center">

**Made with ❤️ for DSA Learners**

Last Updated: 2026-08-14 | [View Latest](../../commits/main)

</div>

