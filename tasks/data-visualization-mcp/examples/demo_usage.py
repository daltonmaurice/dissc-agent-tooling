#!/usr/bin/env python3
"""
Demo script showing how to use the Data Visualization MCP Server functions directly.
This demonstrates the capabilities without needing Claude Desktop.
"""

import sys
import os
from pathlib import Path

# Add current directory to path so we can import our functions
sys.path.append(str(Path(__file__).parent))

from data_viz_server import (
    list_data_files, 
    describe_dataset, 
    generate_correlation_plot, 
    generate_state_comparison
)

def save_base64_image(base64_data, filename):
    """Save a base64 encoded image to a file."""
    import base64
    
    # Extract the base64 part after "data:image/png;base64,"
    if "base64," in base64_data:
        base64_part = base64_data.split("base64,")[1]
    else:
        base64_part = base64_data
    
    # Decode and save
    image_data = base64.b64decode(base64_part)
    with open(filename, 'wb') as f:
        f.write(image_data)
    print(f"✅ Saved image to: {filename}")

def main():
    print("🎯 Data Visualization MCP Server Demo")
    print("=" * 50)
    
    # 1. List available data files
    print("\n📁 1. Available Data Files:")
    print("-" * 30)
    files_result = list_data_files()
    print(files_result)
    
    # 2. Describe a dataset
    print("\n📊 2. Dataset Description:")
    print("-" * 30)
    dataset_name = "obesity-and-diabetes-prevalence-by-state.csv"
    description = describe_dataset(dataset_name)
    print(description)
    
    # 3. Create a correlation plot
    print("\n📈 3. Creating Correlation Plot:")
    print("-" * 30)
    plot_filename = "obesity-vs.-diabetes-prevalence-in-lessspan-data-type_location_greaterunited-stateslessspangreater"
    
    # Try scatter plot
    scatter_result = generate_correlation_plot(plot_filename, "scatter")
    if "Error:" not in scatter_result:
        save_base64_image(scatter_result, "correlation_scatter.png")
        print("✅ Scatter plot created successfully!")
    else:
        print(f"❌ Error creating scatter plot: {scatter_result}")
    
    # Try heatmap
    heatmap_result = generate_correlation_plot(plot_filename, "heatmap")
    if "Error:" not in heatmap_result:
        save_base64_image(heatmap_result, "correlation_heatmap.png")
        print("✅ Heatmap created successfully!")
    else:
        print(f"❌ Error creating heatmap: {heatmap_result}")
    
    # 4. Create state comparison
    print("\n🏛️ 4. Creating State Comparison:")
    print("-" * 30)
    
    # Top 10 states by obesity
    obesity_comparison = generate_state_comparison(plot_filename, "obesity", 10)
    if "Error:" not in obesity_comparison:
        save_base64_image(obesity_comparison, "top_obesity_states.png")
        print("✅ Obesity comparison chart created successfully!")
    else:
        print(f"❌ Error creating obesity comparison: {obesity_comparison}")
    
    # Top 10 states by diabetes
    diabetes_comparison = generate_state_comparison(plot_filename, "diabetes", 10)
    if "Error:" not in diabetes_comparison:
        save_base64_image(diabetes_comparison, "top_diabetes_states.png")
        print("✅ Diabetes comparison chart created successfully!")
    else:
        print(f"❌ Error creating diabetes comparison: {diabetes_comparison}")
    
    print("\n🎉 Demo completed! Check the generated PNG files:")
    print("   - correlation_scatter.png")
    print("   - correlation_heatmap.png") 
    print("   - top_obesity_states.png")
    print("   - top_diabetes_states.png")

if __name__ == "__main__":
    main()
