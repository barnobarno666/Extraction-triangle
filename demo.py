"""
Comprehensive Demo Script for Extraction Triangle Library

This script demonstrates all major features of the extraction-triangle library.
Run this script to see various plotting capabilities and use cases.
"""

import numpy as np
import matplotlib.pyplot as plt
from extraction_triangle import RightTrianglePlot, RightTriangleCoordinates
from extraction_triangle.utils import normalize_data, generate_extraction_curve


def demo_basic_functionality():
    """Demonstrate basic plotting functionality."""
    print("=== Basic Functionality Demo ===")
    
    # Create sample data
    np.random.seed(42)
    n_points = 50
    u = np.random.random(n_points) * 0.8
    v_max = 1 - u
    v = np.random.random(n_points) * v_max
    
    # Create basic plot
    rt_plot = RightTrianglePlot()
    
    # Scatter plot with color coding
    colors = normalize_data(u + v)
    scatter = rt_plot.scatter(u, v, c=colors, s=60, alpha=0.7, 
                             cmap='viridis', label='Random Data')
    
    # Add features
    rt_plot.add_grid(n_lines=10)
    rt_plot.add_labels("Component A", "Component B")
    rt_plot.set_title("Basic Right Triangle Plot")
    rt_plot.add_colorbar(scatter, label='Sum of Components')
    rt_plot.legend()
    
    plt.figure()
    rt_plot.show()


def demo_different_orientations():
    """Demonstrate different triangle orientations."""
    print("=== Different Orientations Demo ===")
    
    orientations = ["bottom-left", "bottom-right", "top-left", "top-right"]
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    # Sample data
    u = np.array([0.1, 0.3, 0.5, 0.7])
    v = np.array([0.8, 0.6, 0.4, 0.2])
    
    for i, orientation in enumerate(orientations):
        ax = axes[i]
        
        # Create coordinate system
        coords = RightTriangleCoordinates(orientation)
        x, y = coords.to_cartesian(u, v)
        
        # Plot triangle boundary
        x_verts, y_verts = coords.get_triangle_vertices()
        ax.plot(x_verts, y_verts, 'k-', linewidth=2)
        
        # Plot data points
        ax.scatter(x, y, c='red', s=100, alpha=0.8, edgecolors='black')
        
        # Customize
        ax.set_aspect('equal')
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.1, 1.1)
        ax.set_title(f"Orientation: {orientation}")
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.suptitle("Right Triangle Plots with Different Orientations", y=1.02)
    plt.show()


def demo_extraction_process():
    """Demonstrate liquid-liquid extraction visualization."""
    print("=== Extraction Process Demo ===")
    
    # Equilibrium data
    u_eq = np.linspace(0.05, 0.85, 15)
    v_eq = 0.9 - 1.1 * u_eq
    v_eq = np.clip(v_eq, 0, 1 - u_eq)
    
    # Operating line
    u_op = np.linspace(0.1, 0.8, 10)
    v_op = 0.85 - u_op
    
    # Create plot
    rt_plot = RightTrianglePlot(figsize=(10, 8))
    
    # Plot equilibrium curve
    rt_plot.plot(u_eq, v_eq, color='blue', linewidth=3, 
                marker='o', markersize=4, label='Equilibrium Curve')
    
    # Plot operating line
    rt_plot.plot(u_op, v_op, color='red', linewidth=2, 
                linestyle='--', label='Operating Line')
    
    # Add feed point
    u_feed, v_feed = 0.4, 0.55
    rt_plot.scatter([u_feed], [v_feed], c='green', s=200, marker='*', 
                   label='Feed Point', edgecolors='black', linewidth=2)
    
    # Add extract and raffinate points
    u_extract, v_extract = 0.15, 0.8
    u_raffinate, v_raffinate = 0.75, 0.2
    
    rt_plot.scatter([u_extract], [v_extract], c='cyan', s=150, marker='s', 
                   label='Extract', edgecolors='black', linewidth=2)
    rt_plot.scatter([u_raffinate], [v_raffinate], c='orange', s=150, marker='s', 
                   label='Raffinate', edgecolors='black', linewidth=2)
    
    # Draw tie line
    rt_plot.plot([u_extract, u_raffinate], [v_extract, v_raffinate], 
                'gray', linewidth=1.5, alpha=0.7, label='Tie Line')
    
    # Customize
    rt_plot.add_grid()
    rt_plot.add_labels("Solute in Extract Phase", "Solvent in Extract Phase")
    rt_plot.set_title("Liquid-Liquid Extraction Diagram")
    rt_plot.legend()
    
    plt.figure()
    rt_plot.show()


def demo_contour_plots():
    """Demonstrate contour plotting capabilities."""
    print("=== Contour Plots Demo ===")
    
    # Generate grid data
    n_grid = 40
    u_grid = []
    v_grid = []
    z_values = []
    
    for i in range(n_grid):
        for j in range(n_grid):
            u = i / (n_grid - 1)
            v = j / (n_grid - 1)
            
            if u + v <= 1:  # Only points inside triangle
                u_grid.append(u)
                v_grid.append(v)
                
                # Example function: selectivity
                selectivity = (u + 0.1) / (v + 0.1)
                z_values.append(selectivity)
    
    u_grid = np.array(u_grid)
    v_grid = np.array(v_grid)
    z_values = np.array(z_values)
    
    # Create contour plot
    rt_plot = RightTrianglePlot(figsize=(10, 8))
    
    # Filled contours
    levels = np.linspace(np.min(z_values), np.max(z_values), 15)
    contour_filled = rt_plot.contourf(u_grid, v_grid, z_values, 
                                     levels=levels, cmap='plasma', alpha=0.8)
    
    # Contour lines
    contour_lines = rt_plot.contour(u_grid, v_grid, z_values, 
                                   levels=levels[::2], colors='white', 
                                   alpha=0.8, linewidths=1)
    
    # Add contour labels
    plt.clabel(contour_lines, inline=True, fontsize=8, fmt='%.1f')
    
    # Add colorbar
    cbar = rt_plot.add_colorbar(contour_filled, label='Selectivity')
    
    # Customize
    rt_plot.add_grid(alpha=0.2)
    rt_plot.add_labels("Component A", "Component B")
    rt_plot.set_title("Selectivity Contour Plot")
    
    plt.figure()
    rt_plot.show()


def demo_multiple_datasets():
    """Demonstrate plotting multiple datasets."""
    print("=== Multiple Datasets Demo ===")
    
    # Generate different datasets
    np.random.seed(123)
    
    # Dataset 1: High selectivity region
    n1 = 30
    u1 = np.random.uniform(0.1, 0.4, n1)
    v1 = np.random.uniform(0.6, 0.9, n1)
    # Ensure valid coordinates
    valid1 = (u1 + v1) <= 1
    u1, v1 = u1[valid1], v1[valid1]
    
    # Dataset 2: Low selectivity region
    n2 = 25
    u2 = np.random.uniform(0.5, 0.8, n2)
    v2 = np.random.uniform(0.1, 0.4, n2)
    valid2 = (u2 + v2) <= 1
    u2, v2 = u2[valid2], v2[valid2]
    
    # Dataset 3: Process curve
    u3 = np.linspace(0.2, 0.7, 20)
    v3 = 0.8 - u3
    valid3 = (u3 + v3) <= 1
    u3, v3 = u3[valid3], v3[valid3]
    
    # Create plot
    rt_plot = RightTrianglePlot(figsize=(10, 8))
    
    # Plot datasets
    rt_plot.scatter(u1, v1, c='blue', s=60, alpha=0.7, marker='o', 
                   label='High Selectivity Zone')
    rt_plot.scatter(u2, v2, c='red', s=60, alpha=0.7, marker='s', 
                   label='Low Selectivity Zone')
    rt_plot.plot(u3, v3, color='green', linewidth=3, marker='D', 
                markersize=6, label='Process Curve')
    
    # Add optimal point
    u_opt, v_opt = 0.3, 0.65
    rt_plot.scatter([u_opt], [v_opt], c='gold', s=200, marker='*', 
                   label='Optimal Point', edgecolors='black', linewidth=2)
    
    # Customize
    rt_plot.add_grid()
    rt_plot.add_labels("Extract Composition", "Raffinate Composition")
    rt_plot.set_title("Multiple Datasets Visualization")
    rt_plot.legend()
    
    plt.figure()
    rt_plot.show()


def demo_advanced_features():
    """Demonstrate advanced features."""
    print("=== Advanced Features Demo ===")
    
    # Create complex visualization
    rt_plot = RightTrianglePlot(figsize=(12, 10))
    
    # Background gradient
    n_bg = 50
    u_bg = []
    v_bg = []
    efficiency = []
    
    for i in range(n_bg):
        for j in range(n_bg):
            u = i / (n_bg - 1)
            v = j / (n_bg - 1)
            
            if u + v <= 1:
                u_bg.append(u)
                v_bg.append(v)
                # Efficiency function
                eff = 1 - ((u - 0.3)**2 + (v - 0.6)**2)
                efficiency.append(max(0, eff))
    
    u_bg = np.array(u_bg)
    v_bg = np.array(v_bg)
    efficiency = np.array(efficiency)
    
    # Background contour
    contour_bg = rt_plot.contourf(u_bg, v_bg, efficiency, levels=20, 
                                 cmap='Blues', alpha=0.6)
    
    # Operating points
    u_points = [0.15, 0.25, 0.35, 0.45]
    v_points = [0.75, 0.65, 0.55, 0.45]
    sizes = [50, 80, 120, 100]
    
    for i, (u, v, s) in enumerate(zip(u_points, v_points, sizes)):
        rt_plot.scatter([u], [v], s=s, c=f'C{i}', alpha=0.8, 
                       edgecolors='black', linewidth=1.5, 
                       label=f'Stage {i+1}')
    
    # Connection lines
    rt_plot.plot(u_points, v_points, 'k--', linewidth=2, alpha=0.7, 
                label='Process Path')
    
    # Add annotations
    for i, (u, v) in enumerate(zip(u_points, v_points)):
        x, y = rt_plot.coordinates.to_cartesian(u, v)
        rt_plot.ax.annotate(f'S{i+1}', (x, y), xytext=(5, 5), 
                           textcoords='offset points', fontsize=10, 
                           fontweight='bold')
    
    # Customize
    rt_plot.add_grid(alpha=0.3)
    rt_plot.add_labels("Component A Fraction", "Component B Fraction")
    rt_plot.set_title("Advanced Extraction Process Visualization")
    rt_plot.add_colorbar(contour_bg, label='Process Efficiency')
    rt_plot.legend(loc='upper right')
    
    plt.figure()
    rt_plot.show()


def main():
    """Run all demonstrations."""
    print("Extraction Triangle Library - Comprehensive Demo")
    print("=" * 50)
    
    # Run all demos
    demo_basic_functionality()
    demo_different_orientations()
    demo_extraction_process()
    demo_contour_plots()
    demo_multiple_datasets()
    demo_advanced_features()
    
    print("\nDemo completed! All plots should be displayed.")
    print("Check the examples/ directory for more detailed examples.")


if __name__ == "__main__":
    main()
