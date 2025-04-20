# Simple test script to check if PGSN can be imported
try:
    from pgsn import *
    print("Successfully imported PGSN module!")
except Exception as e:
    print(f"Error importing PGSN module: {e}")