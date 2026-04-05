"""
Quick test to verify file generation
"""
import sys
print("Python is working!")
print(f"Python version: {sys.version}")
print(f"Working directory: {__file__}")

# Test creating a simple file
with open("test_output.txt", "w") as f:
    f.write("Generator test successful\n")
print("Test file created!")
