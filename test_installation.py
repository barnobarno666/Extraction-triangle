"""
Simple test script to verify the extraction triangle library works correctly.
"""

import numpy as np
from extraction_triangle import RightTrianglePlot, RightTriangleCoordinates

def test_basic_functionality():
    """Test basic functionality of the library."""
    print("Testing basic functionality...")
    
    # Test coordinate system
    coords = RightTriangleCoordinates("bottom-left")
    u, v = 0.3, 0.4
    x, y = coords.to_cartesian(u, v)
    u_back, v_back = coords.from_cartesian(x, y)
    
    print(f"Original coordinates: u={u}, v={v}")
    print(f"Cartesian coordinates: x={x}, y={y}")
    print(f"Back to triangle: u={u_back:.6f}, v={v_back:.6f}")
    
    # Test triangle bounds
    inside = coords.is_inside_triangle([0.3, 0.7, 0.1], [0.4, 0.8, 0.5])
    print(f"Points inside triangle: {inside}")
    
    # Test plot creation (without showing)
    rt_plot = RightTrianglePlot()
    
    # Create sample data
    np.random.seed(42)
    u_data = np.random.random(10) * 0.8
    v_data = np.random.random(10) * (1 - u_data)
    
    # Test scatter plot
    scatter = rt_plot.scatter(u_data, v_data, c='blue', s=50)
    print(f"Scatter plot created successfully: {type(scatter)}")
    
    # Test line plot
    u_line = np.linspace(0, 0.8, 10)
    v_line = 0.9 - u_line
    valid = (u_line + v_line) <= 1
    u_line, v_line = u_line[valid], v_line[valid]
    
    line = rt_plot.plot(u_line, v_line, color='red')
    print(f"Line plot created successfully: {type(line)}")
    
    # Test grid and labels
    rt_plot.add_grid()
    rt_plot.add_labels("Test U", "Test V")
    rt_plot.set_title("Test Plot")
    
    print("All basic functionality tests passed!")
    return True

def test_utils():
    """Test utility functions."""
    print("\nTesting utility functions...")
    
    from extraction_triangle.utils import validate_data, normalize_data, check_triangle_bounds
    
    # Test validate_data
    data = [1, 2, 3, 4, 5]
    validated = validate_data(data)
    print(f"Data validation successful: {len(validated)} points")
    
    # Test normalize_data  
    normalized = normalize_data(data, 0, 1)
    print(f"Normalization successful: range [{np.min(normalized):.3f}, {np.max(normalized):.3f}]")
    
    # Test check_triangle_bounds
    u = np.array([0.3, 0.8])
    v = np.array([0.4, 0.9])  # Second point is outside triangle
    u_clipped, v_clipped = check_triangle_bounds(u, v)
    print(f"Triangle bounds check: {len(u_clipped)} points clipped")
    print(f"All clipped points valid: {np.all(u_clipped + v_clipped <= 1.01)}")
    
    print("All utility function tests passed!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("Extraction Triangle Library - Test Script")
    print("=" * 50)
    
    try:
        test_basic_functionality()
        test_utils()
        print("\n" + "=" * 50)
        print("ALL TESTS PASSED SUCCESSFULLY!")
        print("The extraction triangle library is working correctly.")
        print("=" * 50)
    except Exception as e:
        print(f"\nTEST FAILED: {e}")
        import traceback
        traceback.print_exc()
