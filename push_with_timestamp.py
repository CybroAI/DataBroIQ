#!/usr/bin/env python3
"""
Git Push Script with Timestamp
Automatically commits and pushes all files with current date and time
"""

import subprocess
import os
from datetime import datetime

def push_to_github():
    """
    Add all files, commit with timestamp, and push to GitHub
    """
    try:
        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Update: {current_datetime}"
        
        # Change to the project directory
        project_path = r"C:\Users\mryad\Documents\workspace\databroIQ"
        os.chdir(project_path)
        print(f"📁 Working Directory: {os.getcwd()}")
        print(f"⏰ Timestamp: {current_datetime}\n")
        
        # 1. Add all files
        print("📝 Stage 1: Adding all files...")
        result = subprocess.run(["git", "add", "."], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ All files staged successfully")
        else:
            print(f"❌ Error staging files: {result.stderr}")
            return False
        
        # 2. Check if there are changes to commit
        print("\n📊 Checking for changes...")
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("ℹ️  No changes to commit")
            return True
        
        # 3. Commit with timestamp
        print(f"\n💾 Stage 2: Committing with message: '{commit_message}'")
        result = subprocess.run(
            ["git", "commit", "-m", commit_message],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ Commit successful")
            print(f"   {result.stdout.strip()}")
        else:
            print(f"❌ Error committing: {result.stderr}")
            return False
        
        # 4. Push to remote
        print("\n🚀 Stage 3: Pushing to GitHub...")
        result = subprocess.run(
            ["git", "push", "-u", "origin", "main"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ Push successful!")
            print(f"   {result.stdout.strip()}")
        else:
            print(f"⚠️  Push output: {result.stderr}")
        
        # 5. Show git log
        print("\n📜 Recent commits:")
        result = subprocess.run(
            ["git", "log", "--oneline", "-5"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔄 DataBroIQ - Git Push with Timestamp")
    print("=" * 60)
    
    success = push_to_github()
    
    print("\n" + "=" * 60)
    if success:
        print("✨ Operation completed successfully!")
    else:
        print("⚠️  Operation completed with errors")
    print("=" * 60)
