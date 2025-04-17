import os
import unittest

# Determine problem ID from the script's filename
script_name = os.path.basename(__file__)  # e.g., "test_01-01-01.py"
problem_id = script_name[5:-3]  # Extract "01-01-01" from "test_01-01-01.py"

# Construct the path to the student's solution
unit, chapter, _ = problem_id.split("-")
solution_path = os.path.join(
    f"Unit-{unit}", f"Chapter-{chapter}", f"{problem_id}.py"
)


class TestStudentSolution(unittest.TestCase):
    def test_no_if_statement(self):
        """Fail the test if the student's solution contains the keyword 'if'."""
        with open(solution_path, "r", encoding="utf-8") as f:
            code = f.read()
        if "if" in code:
            print(
                "\n🚨 Test Failed: Your code contains an 'if' statement, which is not allowed.\n"
            )
            self.fail()


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=0)  # Reduce verbosity
    unittest.main(testRunner=runner)
