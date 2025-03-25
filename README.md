# Python Practice

## How to Solve Problems  

1. **Fork and Clone** – Fork this repository and clone it to your local machine.  
2. **Read the Problem** – Open the `XX-XX-XX.md` file in the problem folder to review the instructions.  
3. **Write Your Code** – Create a `XX-XX-XX.py` file in the same folder and implement your solution.  
4. **Test Your Solution** – Run the following command in the terminal:  

   ```sh
    # On macOS/Linux
    python3 test.py XX-XX-XX  

    # On Windows
    python test.py XX-XX-XX  
   ```

**NOTE:** Replace XX-XX-XX with the problem ID (e.g., 01-02-01). This will automatically check your solution using the provided test cases.

## Getting Updates

As new problems are added, you’ll need to pull updates into your fork.


1. **Add Upstream Remote** – Ensure this repository is set as the upstream remote. If it’s not, add it:

    ```sh
    git remote add upstream https://github.com/bassemfarid/python-practice.git
    ```
2. **Fetch and Merge** – Fetch the updates and merge them:

    ```sh
    git fetch upstream
    git merge upstream/main --allow-unrelated-histories --no-commit --no-ff
    ```
    If this is your first merge from upstream, Git may ask you to resolve conflicts or enter a commit message. If not, you can exclude `--allow-unrelated-histories`.
3. **Commit** – Commit the changes you merged in.
    ```sh
    git commit -m "Merged updates from upstream"
    ```
    This will pull new problems and tests into your repository without overwriting your existing solutions.

## File Structure
```
python-practice/
│── test.py  # Central test script
│── README.md
│── main.py  # Code playground without tests
│── .gitignore
│── .venv/
│
├── Unit-01/  # Unit folder
│   ├── Chapter-02/  # Chapter folder
│   │   ├── 01-02-01.py  # Student creates this script
│   │   ├── 01-02-01.md  # Problem details
│   │   ├── ...
│
├── tests/
│   ├── 01-02-01/  # Problem-specific test folder
│   │   ├── test_01-02-01.py  # Unit test script (if needed)
│   │   ├── timeout.txt  # Optional timeout override (if present)
│   │   ├── sample-01.in  # Sample I/O test input
│   │   ├── sample-01.out  # Sample I/O test output
│   │   ├── 1-01.in  # Batch 1, test case 1 input
│   │   ├── 1-01.out  # Batch 1, test case 1 output
│   │   ├── 1-02.in  # Batch 1, test case 2 input
│   │   ├── 1-02.out  # Batch 1, test case 2 output
│   │   ├── 2-01.in  # Batch 2, test case 1 input
│   │   ├── 2-01.out  # Batch 2, test case 1 output
│   │   ├── ...
│   │
│   ├── 01-02-02/  # Another problem's test folder
│   │   ├── sample-01.in
│   │   ├── sample-01.out
│   │   ├── 1-01.in
│   │   ├── 1-01.out
│   │   ├── ...
```