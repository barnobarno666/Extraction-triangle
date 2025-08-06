# Installation and Usage Guide

## Installation

### From Source (Development Installation)

1. Clone or download this repository
2. Navigate to the project directory
3. Install in development mode:

```bash
pip install -e .
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Quick Start

```python
import numpy as np
from extraction_triangle import RightTrianglePlot

# Create sample data
u_data = [0.1, 0.3, 0.5, 0.7]
v_data = [0.8, 0.6, 0.4, 0.2]

# Create plot
rt_plot = RightTrianglePlot()
rt_plot.scatter(u_data, v_data, c='blue', s=100)
rt_plot.add_grid()
rt_plot.add_labels("Component A", "Component B")
rt_plot.set_title("My First Right Triangle Plot")
rt_plot.show()
```

## Running Examples

```bash
# Run basic examples
python examples/basic_example.py

# Run extraction-specific examples
python examples/extraction_example.py

# Run comprehensive demo
python demo.py
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=extraction_triangle
```

## Key Features

- **Right Triangle Coordinate System**: Specialized for binary extraction systems
- **Multiple Orientations**: Support for 4 different triangle orientations
- **Plotting Functions**: Scatter, line, contour, and filled contour plots
- **Grid and Labels**: Customizable grid lines and axis labels
- **Extraction-Specific Tools**: Built-in functions for common extraction scenarios

## Library Structure

```
extraction_triangle/
├── __init__.py           # Main package imports
├── coordinates.py        # Coordinate system handling
├── triangle_plot.py      # Main plotting class
└── utils.py             # Utility functions

examples/
├── basic_example.py      # Basic usage examples
└── extraction_example.py # Extraction-specific examples

tests/
└── test_extraction_triangle.py # Test suite
```

## API Reference

### RightTrianglePlot Class

Main plotting interface:

- `scatter(u, v, **kwargs)` - Create scatter plots
- `plot(u, v, **kwargs)` - Create line plots  
- `contour(u_grid, v_grid, z_values, **kwargs)` - Create contour plots
- `contourf(u_grid, v_grid, z_values, **kwargs)` - Create filled contour plots
- `add_grid(n_lines=10)` - Add grid lines
- `add_labels(u_label, v_label)` - Add axis labels
- `show()` - Display the plot
- `save(filename)` - Save plot to file

### RightTriangleCoordinates Class

Coordinate system handling:

- `to_cartesian(u, v)` - Convert triangle coords to Cartesian
- `from_cartesian(x, y)` - Convert Cartesian coords to triangle
- `is_inside_triangle(u, v)` - Check if points are inside triangle
- `get_triangle_vertices()` - Get triangle boundary vertices

### Utility Functions

- `validate_data(data)` - Validate input data
- `normalize_data(data, min_val, max_val)` - Normalize data to range
- `check_triangle_bounds(u, v)` - Clip coordinates to triangle bounds

## Applications

- Liquid-liquid extraction diagrams
- Binary separation processes
- Phase equilibrium visualization
- Chemical engineering applications
- Process optimization studies

## Support

For questions, issues, or contributions, please check the GitHub repository.
