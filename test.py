import math
import os
import subprocess
import sys
import time


def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_timeout(test_folder):
    timeout_file = os.path.join(test_folder, "timeout.txt")
    if os.path.exists(timeout_file):
        try:
            with open(timeout_file, "r") as f:
                timeout = float(f.read().strip())
                return max(1, min(timeout, 5))  # Clamp between 1 and 5 seconds
        except ValueError:
            pass
    return 2  # Default to 2 seconds


def get_student_script(problem_id):
    unit, chapter, _ = problem_id.split("-")
    location = os.path.join(
        f"Unit-{unit}", f"Chapter-{chapter}", f"{problem_id}.py"
    )
    if not os.path.exists(location):
        print(f"Student script not found: {location}")
        sys.exit(1)
    return location


def run_io_test(test_folder, student_script):
    """Run all I/O tests in the test folder. Stops on batch failure."""
    test_groups = {}
    for f in sorted(os.listdir(test_folder)):
        if f.endswith(".in"):
            group_name = f.rsplit("-", 1)[0]
            if group_name not in test_groups:
                test_groups[group_name] = []
            test_groups[group_name].append(f)

    # Ensures sample tests are run first
    sorted_groups = sorted(
        test_groups.keys(),
        key=lambda x: (x != "sample", int(x) if x.isdigit() else sys.maxsize),
    )

    timeout = get_timeout(test_folder)

    for group in sorted_groups:
        print(f"Running batch {group} tests...")
        for test_file in sorted(test_groups[group]):
            test_name = test_file[:-3]  # Remove .in extension
            expected_output_file = os.path.join(
                test_folder, f"{test_name}.out"
            )
            if not os.path.exists(expected_output_file):
                print(f"Missing expected output file: {expected_output_file}")
                continue

            input_file = os.path.join(test_folder, test_file)
            passed, actual_output, execution_time_ms = run_single_io_test(
                input_file, expected_output_file, student_script, timeout
            )

            if passed:
                print(
                    f"{test_name}: \033[92mPASS\033[0m ({execution_time_ms} ms)"
                )  # Green
            else:
                print(
                    f"{test_name}: \033[91mFAIL\033[0m ({execution_time_ms} ms)"
                )  # Red
                print("\n\033[93mExpected Output:\033[0m")
                print(open(expected_output_file).read().strip())
                print("\n\033[93mActual Output:\033[0m")
                print(actual_output)
                print("=" * 40)
                if group == "sample":
                    print("Sample tests failed. Aborting further testing.")
                    return
                else:
                    print(
                        f"Batch {group} failed. Skipping remaining tests in this batch."
                    )
                    break


def run_single_io_test(
    input_file, expected_output_file, student_script, timeout
):
    with open(input_file, "r") as f:
        input_data = f.read()

    with open(expected_output_file, "r") as f:
        expected_output = f.read().strip()

    try:
        start_time = time.time()
        result = subprocess.run(
            [sys.executable, student_script],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        end_time = time.time()

        execution_time_ms = round((end_time - start_time) * 1000, 2)
        actual_output = result.stdout.strip() if result.stdout else ""

        # Account for floating point errors
        if is_numeric(actual_output) and is_numeric(expected_output):
            passed = math.isclose(
                float(actual_output), float(expected_output), rel_tol=1e-9
            )
        else:
            passed = actual_output == expected_output

        return passed, actual_output, execution_time_ms

    except subprocess.TimeoutExpired:
        return False, "Timed out", timeout * 1000

    except Exception as e:
        return False, str(e), 0


def run_unit_test(test_script):
    """Run a unit test script and return success status."""
    try:
        subprocess.run(["python3", test_script], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Unit test script {test_script} failed.")
        return False


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python test.py <problem_id>")
            sys.exit(1)

        problem_id = sys.argv[1]
        student_script = get_student_script(
            problem_id
        )  # Will exit if not found
        test_folder = os.path.join("tests", problem_id)
        test_script = os.path.join(test_folder, f"test_{problem_id}.py")

        # Ensure the test folder exists
        if not os.path.exists(test_folder):
            print(f"Test folder not found: {test_folder}")
            sys.exit(1)

        # If a unit test script exists, run it. Failure abort further testing.
        if os.path.exists(test_script):
            if not run_unit_test(test_script):
                print("Unit tests failed. Aborting further testing.")
                sys.exit(1)

        # If I/O tests are present, run them
        io_test_files = [
            f for f in os.listdir(test_folder) if f.endswith(".in")
        ]
        if io_test_files:
            run_io_test(test_folder, student_script)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
