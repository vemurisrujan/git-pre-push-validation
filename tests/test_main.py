import subprocess


def test_application_starts():
    result = subprocess.run(
        ["python", "app/main.py"], check=False, capture_output=True, text=True
    )

    assert result.returncode == 0
    assert (
        result.stdout.strip()
        == "Git Pre-Push Validation Application Started Successfully"
    )
    assert (
            result.stdout.strip()
            == "Git Azure Pipeline Validation Application Started Successfully"
        )


def test_application_exit_code():
    result = subprocess.run(
        ["python", "app/main.py"], check=False, capture_output=True, text=True
    )

    assert result.returncode == 0
