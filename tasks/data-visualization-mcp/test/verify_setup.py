#!/usr/bin/env python3
"""
Verification script to test MCP server setup for Claude Desktop.
Run this to ensure everything is configured correctly.
"""

import sys
import os
from pathlib import Path

def check_python_path():
    """Check if Python path is correct."""
    print("🐍 Checking Python path...")
    python_path = sys.executable
    print(f"   Current Python: {python_path}")
    return python_path

def check_mcp_imports():
    """Check if MCP modules can be imported."""
    print("\n📦 Checking MCP imports...")
    try:
        import mcp
        print("   ✅ MCP imported successfully")
        
        from mcp.server.fastmcp import FastMCP
        print("   ✅ FastMCP imported successfully")
        
        return True
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False

def check_data_files():
    """Check if data files exist."""
    print("\n📁 Checking data files...")
    data_dir = Path("../../data")
    if data_dir.exists():
        files = list(data_dir.glob("*.csv"))
        print(f"   ✅ Found {len(files)} CSV files in data directory")
        for file in files:
            print(f"      - {file.name}")
        return True
    else:
        print("   ❌ Data directory not found")
        return False

def test_server_functions():
    """Test the MCP server functions."""
    print("\n🔧 Testing server functions...")
    try:
        from data_viz_server import list_data_files, describe_dataset
        
        # Test list_data_files
        result = list_data_files()
        if "Available Data Files:" in result:
            print("   ✅ list_data_files working")
        else:
            print("   ❌ list_data_files failed")
            return False
        
        # Test describe_dataset
        result = describe_dataset("obesity-and-diabetes-prevalence-by-state.csv")
        if "Dataset:" in result:
            print("   ✅ describe_dataset working")
        else:
            print("   ❌ describe_dataset failed")
            return False
            
        return True
    except Exception as e:
        print(f"   ❌ Server function test failed: {e}")
        return False

def check_config_file():
    """Check if Claude Desktop config file exists."""
    print("\n⚙️ Checking Claude Desktop configuration...")
    config_path = Path.home() / ".config" / "claude-desktop" / "mcp_servers.json"
    
    if config_path.exists():
        print(f"   ✅ Config file exists: {config_path}")
        
        # Read and display config
        with open(config_path, 'r') as f:
            content = f.read()
            print("   📄 Configuration content:")
            print("   " + content.replace('\n', '\n   '))
        return True
    else:
        print(f"   ❌ Config file not found: {config_path}")
        return False

def main():
    """Run all verification checks."""
    print("🔍 Claude Desktop MCP Server Verification")
    print("=" * 50)
    
    checks = [
        check_python_path,
        check_mcp_imports,
        check_data_files,
        test_server_functions,
        check_config_file
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"   ❌ Check failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 50)
    
    if all(results):
        print("🎉 ALL CHECKS PASSED!")
        print("\n✅ Your MCP server is ready for Claude Desktop!")
        print("\n📋 Next steps:")
        print("   1. Launch Claude Desktop")
        print("   2. Start a new conversation")
        print("   3. Ask: 'What MCP tools are available?'")
        print("   4. Try: 'List all available data files'")
    else:
        print("❌ SOME CHECKS FAILED")
        print("\n🔧 Please fix the issues above before using with Claude Desktop")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
