#!/usr/bin/env python3
"""
Script to compile translation files
"""
import os
import subprocess
from pathlib import Path

# Get the directory of this script
SCRIPT_DIR = Path(__file__).parent.absolute()


def compile_translations():
    """Compile translation files"""
    print("Compiling translation files...")
    
    # Path to locales directory
    locales_dir = SCRIPT_DIR / "locales"
    
    # Check if locales directory exists
    if not locales_dir.exists():
        print(f"Error: Directory '{locales_dir}' does not exist")
        return False
    
    try:
        # Try using pybabel directly
        result = subprocess.run(
            ["pybabel", "compile", "-d", str(locales_dir), "-D", "bot"],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Direct pybabel command failed, trying with python -m...")
        
        try:
            # Try using python -m
            result = subprocess.run(
                ["python", "-m", "babel.messages.frontend", "compile", "-d", str(locales_dir), "-D", "bot"],
                check=True,
                capture_output=True,
                text=True
            )
            print(result.stdout)
            return True
        except subprocess.SubprocessError:
            print("Failed to compile translations using python -m")
            print("Please install Babel and try again: pip install Babel")
            return False


if __name__ == "__main__":
    success = compile_translations()
    exit(0 if success else 1) 