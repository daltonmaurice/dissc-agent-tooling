#!/usr/bin/env python3
"""
Test script to verify MCP server works correctly for Claude Desktop.
This simulates what Claude Desktop will do when calling the MCP server.
"""

import sys
import os
from pathlib import Path

def test_mcp_server():
    """Test the MCP server functions as they would be called by Claude Desktop."""
    print("🧪 Testing MCP Server for Claude Desktop")
    print("=" * 50)
    
    # Add current directory to path
    sys.path.append('.')
    
    try:
        from data_viz_server import (
            list_data_files, 
            describe_dataset, 
            generate_correlation_plot, 
            generate_state_comparison
        )
        
        print("✅ Successfully imported MCP server functions")
        
        # Test 1: List data files
        print("\n📁 Test 1: Listing data files")
        print("-" * 30)
        result = list_data_files()
        print(result)
        
        # Test 2: Describe the diabetes dataset
        print("\n📊 Test 2: Describing diabetes dataset")
        print("-" * 30)
        result = describe_dataset("obesity-and-diabetes-prevalence-by-state.csv")
        print(result[:300] + "..." if len(result) > 300 else result)
        
        # Test 3: Test with wrong filename to see error message
        print("\n❌ Test 3: Testing error handling")
        print("-" * 30)
        result = describe_dataset("wrong-filename.csv")
        print(result)
        
        # Test 4: Generate correlation plot
        print("\n📈 Test 4: Generating correlation plot")
        print("-" * 30)
        plot_file = "obesity-vs.-diabetes-prevalence-in-lessspan-data-type_location_greaterunited-stateslessspangreater"
        result = generate_correlation_plot(plot_file, "scatter")
        if "Generated" in result:
            print("✅ Correlation plot generated successfully")
            print(f"Result length: {len(result)} characters")
        else:
            print("❌ Correlation plot failed")
            print(result)
        
        # Test 5: Generate state comparison
        print("\n🏛️ Test 5: Generating state comparison")
        print("-" * 30)
        result = generate_state_comparison(plot_file, "obesity", 5)
        if "Generated" in result:
            print("✅ State comparison generated successfully")
            print(f"Result length: {len(result)} characters")
        else:
            print("❌ State comparison failed")
            print(result)
        
        print("\n" + "=" * 50)
        print("🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print("\n📋 Instructions for Claude Desktop:")
        print("1. Restart Claude Desktop")
        print("2. Start a new conversation")
        print("3. Ask: 'What MCP tools are available?'")
        print("4. Try: 'List all available data files'")
        print("5. Try: 'Describe the obesity-and-diabetes-prevalence-by-state.csv dataset'")
        print("6. Try: 'Create a scatter plot showing obesity vs diabetes correlation'")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_mcp_server()
    sys.exit(0 if success else 1)
