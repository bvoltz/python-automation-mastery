from pathlib import Path
import sys

# Define target project directories dynamically
PROJECT_DIR = Path.home() / "Documents" / "Revit_Automation_Project"
LOG_DIR = PROJECT_DIR / "Logs"

def initialize_workspace():
    print("Checking workspace environment...")
    
    # Verify and build directories without crashing
    if not LOG_DIR.exists():
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        print(f"SUCCESS: Created workspace at {LOG_DIR}")
        
if __name__ == "__main__":
    initialize_workspace()