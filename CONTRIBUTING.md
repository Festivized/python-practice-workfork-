# CONTRIBUTING.md

## Contributing to Python Practice

Thank you for your interest in contributing! This repository is designed to help students practice Python through structured problems with automated I/O testing. Your contributions help improve the quality and variety of problems available to learners.

## How You Can Contribute

You are welcome to contribute in the following ways:

### 📖 Improve Question Clarity
- Edit ##-##-##.md files to fix grammar, improve clarity, or enhance explanations.
- Ensure the problem statement aligns with the expected input/output behavior.

### 🔍 Fix Incorrect I/O Test Cases
- If you find a test case that does not match the expected output, fix it.
- Ensure corrections maintain the intended problem difficulty.

### ✅ Add More Test Cases
- Add edge cases, boundary values, or off-by-one scenarios.
- Name test cases following the existing pattern:
    - ##-##-##.X-YY.in (input file)
    - ##-##-##.X-YY.out (expected output file)
    - X represents test difficulty (1 = easy, 2 = medium, etc.)
    - YY is a sequential number (01, 02, etc.).
    - Example: 01-02-01.2-03.in and 01-02-01.2-03.out.

### ✨ Create New Problems
- Submit a new problem following the existing folder structure (Unit-Chapter).
- Include a ##-##-##.md file with a clear description, input format, output format, and sample cases.
- Add at least 3 test cases (one sample and two additional).
- Ensure your problem is distinct from existing ones.

## Contribution Guidelines

### 1️⃣ Fork the Repository

Click the Fork button on GitHub and clone your fork:

```sh
git clone https://github.com/YOUR-USERNAME/python-practice.git
cd python-practice
```

### 2️⃣ Create a New Branch

Use a meaningful branch name:

```sh
git checkout -b fix-typo-in-01-02-01
```

### 3️⃣ Make Changes & Test Locally
- Modify/add files as needed.
- Run main_test_runner.py to ensure no tests break.

```sh
python main_test_runner.py
```

### 4️⃣ Commit Your Changes

Write a clear commit message:

```sh
git add .
git commit -m "Fixed typo in 01-02-01.md and added edge case"
```

### 5️⃣ Push & Open a Pull Request

```sh
git push origin fix-typo-in-01-02-01
```

- Open a Pull Request (PR) on GitHub.
- Explain your changes briefly.
- A reviewer will provide feedback if needed.

### Style Guide
- Follow PEP 8 for Python code.
- Keep problem descriptions concise and structured.
- Use clear variable names and avoid unnecessary complexity.

## Need Help?

If you have any questions, feel free to open an issue or ask in discussions. Happy coding!

# Prompt

You are a Markdown expert who will help format questions. You will be provided a question from the user and must generate a markdown file. You will do this by:
1. Generate a short (few sentences) story for the question.
2. Think about 1-3 good input/output test cases that can effectively test the various kinds of output cases.
3. Follow the format provided below to generate your response.


Here is the Markdown question format.

# Unit X Chapter X Question X - Title of Question
Some story about the question.

If there is a variable or expression discussed in the question/story, it is represented using a capital letter in LaTeX markdown. For example:

The amount of eggs produced can be measured using the following formula:
$$
\frac{2.5 \times C}{N}
$$
where $C$ represents the number of chickens and $N$ represents the number of nests.

## Input Specification  
Discusses the specifications of the input.

Variables and expressions are again in LaTeX markdown. For example:
There are two lines of input. Each line contains a non-negative integer less than $25$. The first line contains the number of chickens, $C$, and the second line contains the number of nests, $N$, that are involved in laying eggs.


## Output Specification  
Provides the output specifications. 

Outputs are denoted in inline code span. For example:

If the eggs produced is $15$ or greater, output `lots`. Otherwise, output `little`.

or another example without any variables or inline code span:

Output a single integer representing the number of eggs produced.

## Sample Input 1
The sample input section provides a simple case of input provided in a code block. For example:
```
14
12
```

## Output for Sample Input 1
Same as sample input, but as output. For example:
```
True
```

## Explanation of Output for Sample Input 1
This is a short 1-2 sentence explanation. For more complicated algorithms, do not walk through the implementation. You do not need to restate that "the variable is [some input value]". But if you do need to mention the input by itself, put it in inline code span.
If it's within an expression, continue using LaTeX markdown.

An example:

Since $\frac{2.5 \times 14}{12} \approx 2.92$, the eggs produced will be `little`.

## Sample Input 2
This is another case that covers a different result to provide the student a better understanding of the question.

## Output for Sample Input 2
Similar to previous output's formatting.

## Explanation of Output for Sample Input 2
Similar to previous explanation's formatting.