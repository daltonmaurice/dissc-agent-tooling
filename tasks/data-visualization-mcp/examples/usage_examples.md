# Data Visualization MCP Server - Usage Examples

## Overview
This MCP server provides tools for analyzing and visualizing health data from CSV files. It demonstrates the concepts from the NBER presentation about AI agents and MCP architecture.

## Available Tools

### 1. List Data Files
**Tool**: `list_data_files`
**Purpose**: Lists all available data files in the data directory
**Input**: None
**Example Usage**:
```
List all available data files in the data directory
```

### 2. Describe Dataset
**Tool**: `describe_dataset`
**Purpose**: Provides detailed summary statistics and metadata about a specific dataset
**Input**: filename (string)
**Example Usage**:
```
Describe the dataset "obesity-and-diabetes-prevalence-by-state.csv"
```

### 3. Generate Correlation Plot
**Tool**: `generate_correlation_plot`
**Purpose**: Creates scatter plot or heatmap showing correlation between obesity and diabetes
**Input**: 
- filename (string)
- plot_type (optional: "scatter" or "heatmap", default: "scatter")
**Example Usage**:
```
Create a scatter plot showing the correlation between obesity and diabetes using the obesity-vs.-diabetes-prevalence data
```

### 4. Generate State Comparison
**Tool**: `generate_state_comparison`
**Purpose**: Creates bar chart comparing states by health metrics
**Input**:
- filename (string)
- metric (string: "obesity" or "diabetes")
- top_n (integer, default: 10)
**Example Usage**:
```
Show me the top 10 states with highest obesity rates using the obesity vs diabetes data
```

## Sample Workflow

1. **Explore Available Data**:
   - Use `list_data_files` to see what datasets are available

2. **Understand the Data**:
   - Use `describe_dataset` to get summary statistics and understand the structure

3. **Create Visualizations**:
   - Use `generate_correlation_plot` to explore relationships between variables
   - Use `generate_state_comparison` to compare states by specific metrics

## Data Files
- `obesity-and-diabetes-prevalence-by-state.csv`: Diabetes prevalence data by state
- `obesity-vs.-diabetes-prevalence-in-lessspan-data-type_location_greaterunited-stateslessspangreater`: Combined obesity and diabetes data by state

## Technical Notes
- All plots are returned as base64 encoded PNG images
- The server handles missing data gracefully
- Error messages provide helpful guidance for troubleshooting
- Supports both scatter plots and correlation heatmaps
