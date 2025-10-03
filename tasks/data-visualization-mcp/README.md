# Data Visualization MCP Server

A Model Context Protocol (MCP) server that provides tools for listing and visualizing health data from CSV files. This server demonstrates MCP concepts for AI agents in economic research workflows, as discussed in the NBER presentation.

## Features

- **List Data Files**: Browse available datasets in the data directory
- **Dataset Analysis**: Get detailed statistics and metadata about datasets
- **Correlation Visualization**: Create scatter plots and heatmaps showing relationships between variables
- **State Comparisons**: Generate bar charts comparing states by health metrics

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure your data files are in the `../../data/` directory (relative to this script)

## Usage

### With Cursor IDE
The server is configured to work with Cursor IDE via the `.cursor/mcp.json` configuration file. Once the dependencies are installed, the server will be available as an MCP tool in Cursor.

### Manual Testing
Run the test script to verify functionality:
```bash
python test_server.py
```

### Direct Server Execution
```bash
python data_viz_server.py /path/to/data/directory
```

## Available Tools

1. **list_data_files**: Lists all data files with metadata
2. **describe_dataset**: Provides summary statistics for a dataset
3. **generate_correlation_plot**: Creates correlation visualizations
4. **generate_state_comparison**: Generates state comparison charts

## Data Requirements

The server expects CSV files with specific column structures:
- For correlation analysis: files with 'Obesity' and 'Diabetes' columns
- For state comparisons: files with 'geography' column and metric columns

## Architecture

This implementation follows the MCP architecture:
- **Host**: Cursor IDE or other MCP-compatible host
- **Client**: MCP client embedded in the host
- **Server**: This Python application using STDIO transport

## Error Handling

The server includes comprehensive error handling for:
- Missing files
- Invalid data formats
- Malformed CSV files
- Missing required columns

## Security

- File path validation prevents directory traversal
- Input sanitization for plot parameters
- Local-only access via STDIO transport
- No network exposure

## Example Workflow

1. Use `list_data_files` to explore available datasets
2. Use `describe_dataset` to understand data structure
3. Use `generate_correlation_plot` to explore relationships
4. Use `generate_state_comparison` to compare states

This server demonstrates how MCP enables AI agents to interact with data analysis tools in a standardized, secure manner.
