"""Test the usage output of the application."""


# ----------------------------------------------------------------------------
#  MODULE IMPORTS
# ----------------------------------------------------------------------------
import subprocess


# ----------------------------------------------------------------------------
#  TESTS
# ----------------------------------------------------------------------------
def test_usage(executable):
    """Test the usage output when the '-h' or '--help' option is used."""
    assert "usage:" in subprocess.run(executable + ["--help"], text=True, check=False, stdout=subprocess.PIPE).stdout


# ----------------------------------------------------------------------------
#  EOF
# ----------------------------------------------------------------------------
