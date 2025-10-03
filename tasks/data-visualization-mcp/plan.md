# Implementation Plan: Data Visualization MCP Server

## Overview
Create a locally hosted MCP server that can list and generate figures from health data in the `@data/` directory. This server will demonstrate the concepts from the NBER presentation about AI agents and MCP architecture.

## Architecture Design

### MCP Server Components
1. **Host**: Local development environment (Cursor/VS Code)
2. **Client**: MCP client embedded in the host
3. **Server**: Python-based MCP server with STDIO transport

### Tool Manifest
Based on the research findings, implement these tools:

#### 1. `list_data_files`
- **Purpose**: List all available data files in the data directory
- **Input**: None
- **Output**: Array of file names with metadata
- **Implementation**: Scan data directory and return file information

#### 2. `describe_dataset`
- **Purpose**: Provide summary statistics and metadata about a specific dataset
- **Input**: filename (string)
- **Output**: Dataset description including columns, shape, basic statistics
- **Implementation**: Load CSV, analyze structure, return summary

#### 3. `generate_correlation_plot`
- **Purpose**: Create scatter plot showing correlation between obesity and diabetes
- **Input**: filename (string), plot_type (optional: "scatter", "heatmap")
- **Output**: Base64 encoded image
- **Implementation**: Use matplotlib/seaborn to create visualizations

#### 4. `generate_state_comparison`
- **Purpose**: Create bar chart comparing states by health metrics
- **Input**: filename (string), metric (string: "obesity" or "diabetes"), top_n (integer)
- **Output**: Base64 encoded image
- **Implementation**: Generate bar charts for state comparisons

## Implementation Steps

### Phase 1: Environment Setup
1. Create project structure
2. Set up Python virtual environment
3. Install dependencies: `mcp[cli]`, `pandas`, `matplotlib`, `seaborn`
4. Create requirements.txt

### Phase 2: Core Server Implementation
1. Create main server file (`data_viz_server.py`)
2. Implement MCP server class with STDIO transport
3. Define tool schemas using JSON Schema
4. Implement error handling and logging

### Phase 3: Tool Implementation
1. Implement `list_data_files` tool
2. Implement `describe_dataset` tool
3. Implement `generate_correlation_plot` tool
4. Implement `generate_state_comparison` tool

### Phase 4: Testing and Configuration
1. Create `.cursor/mcp.json` configuration
2. Test with MCP Inspector
3. Create example usage documentation
4. Add data validation and error handling

## File Structure
```
tasks/data-visualization-mcp/
├── research.md
├── plan.md
├── data_viz_server.py
├── requirements.txt
├── .cursor/
│   └── mcp.json
└── examples/
    └── usage_examples.md
```

## Dependencies
- `mcp[cli]`: MCP Python SDK with CLI support
- `pandas`: Data manipulation and analysis
- `matplotlib`: Basic plotting
- `seaborn`: Statistical visualization
- `numpy`: Numerical operations

## Security Considerations
- File path validation to prevent directory traversal
- Input sanitization for plot parameters
- Error handling for malformed data files
- Local-only access (STDIO transport)

## Success Criteria
1. Server successfully lists data files
2. Server generates meaningful visualizations
3. Server handles errors gracefully
4. Integration works with Cursor IDE
5. Demonstrates MCP concepts from presentation

## Future Enhancements
- Support for additional data formats
- More visualization types (maps, time series)
- Data filtering and querying capabilities
- Export functionality for generated plots
