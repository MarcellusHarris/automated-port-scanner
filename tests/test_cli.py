import subprocess


def test_help_option():
    """Test that the scanner script prints help and exits with code 0."""
    result = subprocess.run(['python','scanner.py','--help'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage" in result.stdout.lower() or "options" in result.stdout.lower()

def test_basic_run(monkeypatch):
    """A placeholder test for basic run."""
    assert True
