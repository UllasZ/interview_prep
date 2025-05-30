"""
# Problem Statement
- Given two strings, str1, and str2, where str1 contains exactly one character more than str2,
  find the indices of the characters in str1 that can be removed to make str1 equal to str2.
- Return the array of indices in increasing order. If it is not possible, return the array [-1].

Note: Use 0-based indexing.

Example:
    str1 = "abdgggda"
    str2 = "abdggda"

    Any "g" character at positions 3, 4, or 5 can be deleted to obtain str2. Return [3, 4, 5].

Input Format:
    Function Description:
        - Complete the function getRemovableIndices in the editor below.
        - getRemovableIndices has the following parameters:
        - string str1: the string to modify
        - string str2: the target string


Output Format:
     - int[]: the indices of characters that can be removed from str1 in ascending order, or [-1]
       if it is not possible to match str2

Constraints:
    --> 2 ≤ |str1| ≤ 2 * 10^5
    --> 1 ≤ |str2| ≤ 2 * 10^5
    --> |str1| = |str2| + 1
    --> str1 and str2 only contain lowercase English letters.
"""

def find_removal_indices(str1: str, str2: str) -> list:
    if len(str1) != len(str2) + 1:
        return [-1]

    result = []
    for i in range(len(str1)):
        if str1[:i] + str1[i+1:] == str2:
            result.append(i)

    return result if result else [-1]


str1 = "abdgggda"
str2 = "abdggda"
print(find_removal_indices(str1, str2))

"""
Your overall rating is 3/5
Code Quality: 3/5
    - Your code demonstrates a clear and straightforward approach with good readability and structure.
    - You implemented proper input validation by checking string lengths at the start.
    - However, there's room for improvement in terms of efficiency and optimization.
    - The string slicing operations in your solution, while making the code readable,
      led to performance issues with larger inputs.
    - Consider using more efficient data structures or algorithms for better performance.
    - Your code follows Python conventions and is well-organized,
      but could benefit from additional comments explaining the logic and approach.

Problem Solving: 2/5
    - While you were able to come up with a working solution for smaller inputs,
      your approach showed limitations with handling larger test cases.
    - You identified the basic requirement of finding removable indices but didn't optimize the solution
      when faced with timeout issues.
    - Despite multiple attempts and hints about performance problems,
      you didn't explore alternative approaches to improve efficiency.
    - To improve, focus on analyzing the time complexity of your solutions early in the problem-solving process and
      consider multiple approaches before implementation.
    - Practice problems with large inputs to develop more efficient solutions.

Language Proficiency: 3/5
    - You demonstrated good familiarity with Python's basic string operations and list manipulations.
    - Your use of string slicing and list operations shows comfort with the language's built-in features.
    - However, there's room to improve in utilizing more efficient Python-specific features and optimizations.
    - To enhance your Python proficiency, explore more advanced Python features and standard library functions
      that could help optimize similar string manipulation problems.
    - Practice using different data structures available in Python and understand their performance characteristics.

Technical Communication: 2/5
    - Your communication during the interview was minimal.
    - When faced with performance issues, you didn't explain your thought process or discuss potential alternatives.
    - When asked about exploring a different approach, you responded with a simple 'no' without elaborating on your reasoning.
    - To improve, practice explaining your approach, discussing trade-offs,
      and engaging in technical discussions about potential solutions.
    - Don't hesitate to think aloud and share your reasoning, as this helps interviewers
      understand your problem-solving process.
"""

"""
Here are some valuable tips to improve your problem-solving skills:

1.  Start with Problem Analysis 🔍
*   Always take time to understand the problem completely
*   Write down example cases, including edge cases
*   Break down the problem into smaller sub-problems
*   Identify patterns and constraints before coding

2.  Think About Efficiency Early 🚀

*   Consider the input size and constraints
*   Analyze time and space complexity before implementing
*   Start with a brute force solution, but always think about optimization
*   Look for opportunities to use appropriate data structures (hash maps, sets, etc.)

3.  Develop a Systematic Approach 📝
*   Follow the UMPIRE method:
*   Understand the problem
*   Match the problem with known patterns
*   Plan your approach
*   Implement the solution
*   Review your code
*   Evaluate other approaches

4.  Practice Communication 🗣️
*   Explain your thought process out loud
*   Discuss trade-offs between different approaches
*   Ask clarifying questions when needed
*   Share your reasoning behind choosing a particular solution

5.  Common Optimization Techniques 💡
*   Two-pointer technique for array/string problems
*   Hash maps for O(1) lookups
*   Sliding window for substring problems
*   Dynamic programming for optimization problems

"""