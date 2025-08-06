"""
Test the new solubili    # Test tie line (conjugate curve)
    print("Testing tie line...")
    conjugate_line = rt_plot.add_conjugate_line(
        0.3, 0.4, 0.3,  # Phase 1
        0.7, 0.1, 0.2,  # Phase 2
        color='red', label='Test Tie Line'
    )
    print(f"Tie line created: {type(conjugate_line)}")ope and tie line functionality.
"""

import numpy as np
from extraction_triangle import RightTrianglePlot

def test_envelope_and_tie_lines():
    """Test the new solubility envelope and tie line features."""
    print("Testing solubility envelope and tie line functionality...")
    
    # Create plot
    rt_plot = RightTrianglePlot()
    
    # Test solubility envelope
    print("Testing solubility envelope...")
    a_data = [0.01, 0.3, 0.5, 0.7, 0.01]
    b_data = [0.8, 0.6, 0.4, 0.2, 0.8]
    c_data = [0.1, 0.1, 0.1, 0.1, 0.1]
    
    envelope_line = rt_plot.add_solubility_envelope(
        a_data, b_data, c_data,
        interpolate=True, color='blue', label='Test Envelope'
    )
    print(f"Solubility envelope created: {type(envelope_line)}")
    
    # Test conjugate line
    print("Testing conjugate line...")
    conjugate_line = rt_plot.add_conjugate_line(
        0.2, 0.7, 0.1,  # Phase 1
        0.6, 0.3, 0.1,  # Phase 2
        color='red', label='Test Conjugate Line'
    )
    print(f"Conjugate line created: {type(conjugate_line)}")
    
    # Test multiple tie lines
    print("Testing multiple tie lines...")
    phase1_data = {
        'a': [0.1, 0.2, 0.3],
        'b': [0.8, 0.7, 0.6],
        'c': [0.1, 0.1, 0.1]
    }
    
    phase2_data = {
        'a': [0.5, 0.6, 0.7],
        'b': [0.4, 0.3, 0.2],
        'c': [0.1, 0.1, 0.1]
    }
    
    tie_lines = rt_plot.add_tie_lines(
        phase1_data, phase2_data,
        color='green', show_points=True
    )
    print(f"Tie lines created: {len(tie_lines)} lines")
    
    # Test plait point
    print("Testing plait point...")
    plait_point = rt_plot.add_plait_point(
        0.4, 0.5, 0.1,
        color='purple', label='Test Plait Point'
    )
    print(f"Plait point created: {type(plait_point)}")
    
    # Test extraction region
    print("Testing extraction region...")
    envelope_data = {
        'a': a_data,
        'b': b_data,
        'c': c_data
    }
    
    region_added = rt_plot.add_extraction_region(
        envelope_data, fill_color='lightblue', label='Test Region'
    )
    print(f"Extraction region added: {region_added}")
    
    # Add labels and show
    rt_plot.add_labels("Component A", "Component B", "Component C")
    rt_plot.set_title("Test: Solubility Envelope and Tie Lines")
    rt_plot.legend()
    
    print("All functionality tests passed!")
    return rt_plot

if __name__ == "__main__":
    plot = test_envelope_and_tie_lines()
    plot.show()
