import subprocess

def test_application_starts():
    result = subprocess.run(
        ["python", "app/main.py"], check=False, capture_output=True, text=True
    )

    assert result.returncode == 0

    expected_output = [
        "Git Pre-Push Validation Application Started Successfully",
        "Git Azure Pipeline Validation Application Started Successfully",
    ]

    actual_output = result.stdout.strip().splitlines()

    assert actual_output == expected_output

def test_application_exit_code():
    result = subprocess.run(
        ["python", "app/main.py"], check=False, capture_output=True, text=True
    )

    assert result.returncode == 0
