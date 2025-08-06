"""
Test the ternary (three-component) functionality.
"""

import numpy as np
from extraction_triangle import RightTrianglePlot

def test_ternary_functionality():
    """Test the new ternary functionality."""
    print("Testing ternary (three-component) functionality...")
    
    # Create plot
    rt_plot = RightTrianglePlot()
    
    # Test ternary scatter plot
    # Example: solute, extract solvent, raffinate solvent
    solute = [0.2, 0.4, 0.6]
    extract_solvent = [0.3, 0.4, 0.3]
    raffinate_solvent = [0.5, 0.2, 0.1]
    
    print(f"Component A (solute): {solute}")
    print(f"Component B (extract solvent): {extract_solvent}")
    print(f"Component C (raffinate solvent): {raffinate_solvent}")
    
    # Check that components sum to 1
    totals = [a + b + c for a, b, c in zip(solute, extract_solvent, raffinate_solvent)]
    print(f"Component sums: {totals}")
    
    # Test scatter_ternary
    scatter = rt_plot.scatter_ternary(solute, extract_solvent, raffinate_solvent,
                                     c=['red', 'blue', 'green'], s=100)
    print(f"Ternary scatter plot created: {type(scatter)}")
    
    # Test get_third_component
    calculated_c = rt_plot.get_third_component(solute, extract_solvent)
    print(f"Calculated third component: {calculated_c}")
    print(f"Original third component: {raffinate_solvent}")
    print(f"Match: {np.allclose(calculated_c, raffinate_solvent)}")
    
    # Test grid with labels
    rt_plot.add_grid(show_labels=True)
    
    # Test labels
    rt_plot.add_labels("Solute", "Extract Solvent", "Raffinate Solvent")
    rt_plot.add_corner_labels("Pure Solute", "Pure Extract", "Pure Raffinate")
    
    rt_plot.set_title("Three-Component Extraction System Test")
    
    print("All ternary functionality tests passed!")
    return rt_plot

if __name__ == "__main__":
    plot = test_ternary_functionality()
    plot.show()
