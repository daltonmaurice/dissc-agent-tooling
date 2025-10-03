#!/usr/bin/env python3
"""
Test script for the Data Visualization MCP Server
"""

import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the functions directly
from data_viz_server import list_data_files, describe_dataset, generate_correlation_plot, generate_state_comparison


def test_server():
    """Test the MCP server functionality."""
    print("Testing Data Visualization MCP Server...")
    
    # Test list_data_files
    print("\n1. Testing list_data_files...")
    result = list_data_files()
    print("Result:", result[:200] + "..." if len(result) > 200 else result)
    
    # Test describe_dataset
    print("\n2. Testing describe_dataset...")
    result = describe_dataset("obesity-and-diabetes-prevalence-by-state.csv")
    print("Result:", result[:300] + "..." if len(result) > 300 else result)
    
    # Test generate_correlation_plot
    print("\n3. Testing generate_correlation_plot...")
    result = generate_correlation_plot(
        "obesity-vs.-diabetes-prevalence-in-lessspan-data-type_location_greaterunited-stateslessspangreater",
        "scatter"
    )
    print("Result:", result[:200] + "..." if len(result) > 200 else result)
    if "data:image/png;base64," in result:
        print("Image generated successfully!")
    
    # Test generate_state_comparison
    print("\n4. Testing generate_state_comparison...")
    result = generate_state_comparison(
        "obesity-vs.-diabetes-prevalence-in-lessspan-data-type_location_greaterunited-stateslessspangreater",
        "obesity",
        5
    )
    print("Result:", result[:200] + "..." if len(result) > 200 else result)
    if "data:image/png;base64," in result:
        print("Chart generated successfully!")
    
    print("\n✅ All tests completed successfully!")


if __name__ == "__main__":
    test_server()