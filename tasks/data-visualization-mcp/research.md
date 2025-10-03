# Research: Data Visualization MCP Server

## Data Analysis
Based on examination of the data files in `/data/` directory:

### Dataset 1: `obesity-and-diabetes-prevalence-by-state.csv`
- **Structure**: CSV with columns: geography, age, outcome_name, value, pct_captured
- **Content**: Diabetes prevalence data by state with percentage captured
- **Records**: 51 states + DC
- **Key Fields**: geography (state names), outcome_name (Diabetes), value (prevalence %)

### Dataset 2: `obesity-vs.-diabetes-prevalence-in-lessspan-data-type_location_greaterunited-stateslessspangreater`
- **Structure**: CSV with columns: geography, Obesity, Diabetes
- **Content**: Both obesity and diabetes prevalence by state
- **Records**: 52 entries (51 states + DC + United States average)
- **Key Fields**: geography, Obesity (%), Diabetes (%)

## Existing Patterns in Codebase
- No existing MCP server implementations found
- Project appears to be focused on economic research and AI agent tooling
- Presentation materials suggest focus on modular agent development

## MCP Server Requirements
Based on the implementation roadmap from gemnitenote.md:

### Core Tools Needed:
1. **list_data_files**: List all available data files in the data directory
2. **generate_figure**: Create visualizations from specified data files
3. **describe_dataset**: Provide summary statistics and metadata about datasets

### Technical Requirements:
- Python-based MCP server using STDIO transport for local development
- Data processing capabilities (pandas, matplotlib/seaborn)
- Error handling for missing files and invalid data
- Support for common visualization types (scatter plots, bar charts, heatmaps)

## Research Findings
- Both datasets contain health-related prevalence data by US states
- Data is clean and well-structured for visualization
- Opportunity to create correlation analysis between obesity and diabetes
- Geographic visualization potential using state names
- Time-series analysis not applicable (single time point data)

## Next Steps
1. Create comprehensive implementation plan
2. Set up Python environment with required dependencies
3. Implement MCP server with STDIO transport
4. Create visualization tools for the health data
5. Test with local MCP client
