#!/usr/bin/env python3
"""
Data Visualization MCP Server

A Model Context Protocol server that provides tools for listing and visualizing
health data from CSV files. This server demonstrates MCP concepts for AI agents
in economic research workflows.

Based on the implementation roadmap from the MCP documentation.
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from mcp.server.fastmcp import FastMCP


# Initialize the MCP server
mcp = FastMCP("DataVisualizationServer")

# Global data directory path - use absolute path to avoid issues with working directory
# Use environment variable if available, otherwise fall back to absolute path
DATA_DIR = Path(os.environ.get("DATA_DIR", "/Users/mad265/git-pub/dissc-agent-tooling/data"))

# Output directory for saving generated images
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/Users/mad265/git-pub/dissc-agent-tooling/output/images"))

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


@mcp.tool()
def list_data_files() -> str:
    """Lists all available data files in the data directory with basic metadata including file size and type."""
    try:
        if not DATA_DIR.exists():
            return f"Error: Data directory '{DATA_DIR}' does not exist."
        
        files = []
        for file_path in DATA_DIR.glob("*"):
            if file_path.is_file():
                stat = file_path.stat()
                files.append({
                    "name": file_path.name,
                    "size_bytes": stat.st_size,
                    "size_mb": round(stat.st_size / (1024 * 1024), 2),
                    "extension": file_path.suffix
                })
        
        if not files:
            return "No data files found in the data directory."
        
        # Format as a nice table
        result = "Available Data Files:\n\n"
        result += "| Filename | Size (MB) | Type |\n"
        result += "|----------|----------|------|\n"
        
        for file_info in files:
            result += f"| {file_info['name']} | {file_info['size_mb']} | {file_info['extension']} |\n"
        
        return result
        
    except Exception as e:
        return f"Error listing data files: {str(e)}"


@mcp.tool()
def describe_dataset(filename: str) -> str:
    """Provides detailed summary statistics and metadata about a specific dataset including column information, data types, and basic statistics."""
    try:
        file_path = DATA_DIR / filename
        
        if not file_path.exists():
            # List available files to help user
            available_files = [f.name for f in DATA_DIR.glob("*.csv")] if DATA_DIR.exists() else []
            return f"Error: File '{filename}' not found in data directory. Available files: {available_files}"
        
        # Load the dataset
        df = pd.read_csv(file_path)
        
        # Generate description
        result = f"Dataset: {filename}\n"
        result += f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n\n"
        
        result += "Columns:\n"
        for col in df.columns:
            dtype = df[col].dtype
            null_count = df[col].isnull().sum()
            result += f"  - {col}: {dtype} ({null_count} null values)\n"
        
        result += "\nFirst 5 rows:\n"
        result += df.head().to_string()
        
        result += "\n\nBasic Statistics:\n"
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            result += df[numeric_cols].describe().to_string()
        else:
            result += "No numeric columns found for statistical analysis."
        
        return result
        
    except Exception as e:
        return f"Error describing dataset: {str(e)}"


@mcp.tool()
def generate_correlation_plot(filename: str, plot_type: str = "scatter") -> str:
    """Creates a scatter plot or heatmap showing the correlation between obesity and diabetes prevalence by state. Returns a base64 encoded image."""
    try:
        file_path = DATA_DIR / filename
        
        if not file_path.exists():
            return f"Error: File '{filename}' not found in data directory."
        
        # Load the dataset
        df = pd.read_csv(file_path)
        
        # Check if we have the required columns
        if 'Obesity' not in df.columns or 'Diabetes' not in df.columns:
            return "Error: Dataset must contain 'Obesity' and 'Diabetes' columns for correlation analysis."
        
        # Filter out any rows with missing data
        df_clean = df.dropna(subset=['Obesity', 'Diabetes'])
        
        if len(df_clean) == 0:
            return "Error: No valid data points found for correlation analysis."
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        
        if plot_type == "scatter":
            plt.scatter(df_clean['Obesity'], df_clean['Diabetes'], alpha=0.7, s=50)
            plt.xlabel('Obesity Prevalence (%)')
            plt.ylabel('Diabetes Prevalence (%)')
            plt.title('Obesity vs Diabetes Prevalence by State')
            
            # Add correlation coefficient
            correlation = df_clean['Obesity'].corr(df_clean['Diabetes'])
            plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
                    transform=plt.gca().transAxes, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
            
            # Add trend line
            z = np.polyfit(df_clean['Obesity'], df_clean['Diabetes'], 1)
            p = np.poly1d(z)
            plt.plot(df_clean['Obesity'], p(df_clean['Obesity']), "r--", alpha=0.8)
            
        elif plot_type == "heatmap":
            # Create correlation matrix
            corr_data = df_clean[['Obesity', 'Diabetes']].corr()
            sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0,
                       square=True, cbar_kws={'shrink': 0.8})
            plt.title('Correlation Heatmap: Obesity vs Diabetes')
        else:
            return f"Error: Invalid plot type '{plot_type}'. Use 'scatter' or 'heatmap'."
        
        plt.tight_layout()
        
        # Save image to file instead of returning base64
        output_filename = f"{filename.split('.')[0]}_{plot_type}_correlation.png"
        output_path = OUTPUT_DIR / output_filename
        plt.savefig(output_path, format='png', dpi=150, bbox_inches='tight')
        plt.close()
        
        return f"Generated {plot_type} plot for {filename}. Image saved to: {output_path}"
        
    except Exception as e:
        return f"Error generating correlation plot: {str(e)}"


@mcp.tool()
def list_generated_images() -> str:
    """Lists all generated visualization images in the output directory with file sizes and creation dates."""
    try:
        if not OUTPUT_DIR.exists():
            return f"Error: Output directory '{OUTPUT_DIR}' does not exist."
        
        images = []
        for file_path in OUTPUT_DIR.glob("*.png"):
            if file_path.is_file():
                stat = file_path.stat()
                images.append({
                    "name": file_path.name,
                    "size_bytes": stat.st_size,
                    "size_kb": round(stat.st_size / 1024, 1),
                    "created": stat.st_mtime
                })
        
        if not images:
            return "No generated images found in the output directory."
        
        # Sort by creation time (newest first)
        images.sort(key=lambda x: x['created'], reverse=True)
        
        # Format as a nice table
        result = "Generated Visualization Images:\n\n"
        result += "| Filename | Size (KB) | Created |\n"
        result += "|----------|-----------|--------|\n"
        
        for img in images:
            from datetime import datetime
            created_str = datetime.fromtimestamp(img['created']).strftime('%Y-%m-%d %H:%M')
            result += f"| {img['name']} | {img['size_kb']} | {created_str} |\n"
        
        return result
        
    except Exception as e:
        return f"Error listing generated images: {str(e)}"


@mcp.tool()
def generate_state_comparison(filename: str, metric: str, top_n: int = 10) -> str:
    """Creates a bar chart comparing states by health metrics (obesity or diabetes prevalence). Shows top N states by default."""
    try:
        file_path = DATA_DIR / filename
        
        if not file_path.exists():
            return f"Error: File '{filename}' not found in data directory."
        
        # Load the dataset
        df = pd.read_csv(file_path)
        
        # Check if we have the required columns (case insensitive)
        metric_col = None
        for col in df.columns:
            if col.lower() == metric.lower():
                metric_col = col
                break
        
        if metric_col is None:
            return f"Error: Column '{metric}' not found in dataset. Available columns: {list(df.columns)}"
        
        if 'geography' not in df.columns:
            return "Error: Dataset must contain 'geography' column for state comparison."
        
        # Filter out any rows with missing data
        df_clean = df.dropna(subset=[metric_col, 'geography'])
        
        if len(df_clean) == 0:
            return "Error: No valid data points found for state comparison."
        
        # Sort by metric and get top N
        df_sorted = df_clean.sort_values(metric_col, ascending=False).head(top_n)
        
        # Create the plot
        plt.figure(figsize=(12, 8))
        bars = plt.bar(range(len(df_sorted)), df_sorted[metric_col], 
                      color='steelblue', alpha=0.7)
        
        plt.xlabel('State')
        plt.ylabel(f'{metric.title()} Prevalence (%)')
        plt.title(f'Top {top_n} States by {metric.title()} Prevalence')
        plt.xticks(range(len(df_sorted)), df_sorted['geography'], rotation=45, ha='right')
        
        # Add value labels on bars
        for i, (bar, value) in enumerate(zip(bars, df_sorted[metric_col])):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{value:.1f}%', ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        
        # Save image to file instead of returning base64
        output_filename = f"{filename.split('.')[0]}_{metric}_top{top_n}_comparison.png"
        output_path = OUTPUT_DIR / output_filename
        plt.savefig(output_path, format='png', dpi=150, bbox_inches='tight')
        plt.close()
        
        return f"Generated state comparison chart for {metric} (top {top_n} states). Image saved to: {output_path}"
        
    except Exception as e:
        return f"Error generating state comparison: {str(e)}"


if __name__ == "__main__":
    # Run the server
    mcp.run()