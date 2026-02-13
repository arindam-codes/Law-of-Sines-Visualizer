# Law of Sines Visualizer

## Overview
This project is a **computational geometry exercise** inspired by an advanced drawing problem from  
*Think Python (3rd Edition) — Allen B. Downey*.

The goal is to construct a **generalized geometric drawing method** that approximates a circle using
polygonal segments, derived purely from trigonometric relationships rather than hard-coded geometry.

---

## Problem Statement
The task is to design a function `draw_pie()` that can:

- draw a circle of **any radius**
- approximate the circle using **any number of sides (n)**
- rely only on a **single primitive drawing function** based on triangles

This forces the solution to be **fully parametric** and **mathematically grounded**.

---

## Geometric Insight
The circle is approximated by dividing it into **n identical isosceles triangles**, each subtending
an angle θ between adjacent sides.

Using the **Law of Sines**, the base length of each triangle segment is derived as:
base = (sin(fi) / sin(θ)) * radius
Where:
- `θ` is the angle between adjacent sides of the polygon
- `φ` is the remaining equal angle of the isosceles triangle
- `radius` is the radius of the target circle

This formulation allows the circle approximation to scale smoothly with both radius and resolution.

---

## Iterations & Corrections

During development, several incorrect geometric assumptions were tested
and visually analyzed before arriving at the final formulation.

These intermediate sketches helped identify:
- incorrect angle relationships
- scaling inconsistencies
- limitations of naive constructions


## Visual Reasoning & Results

The geometry was reasoned visually before implementation.
Below are sketches and generated outputs that validate the trigonometric model.

### Hand-drawn geometric reasoning
![Geometric Reasoning](./images/handdrawn.jpg)

### Early geometric attempts (incorrect)
![Initial incorrect sketch](./images/incorrect.png)
![Initial incorrect sketch](./images/incorrect2.png)

### Refined reasoning after correction
![Output example 1](./images/corrected1.png)
![Output example 2](./images/corrected2.png)
![Output example 2](./images/corrected3.png)
![Output example 2](./images/pic.jpg)

---

## Implementation Approach
- Geometry is expressed purely through **trigonometric relationships**
- A single generalized triangle-drawing primitive is reused
- Higher-level shapes emerge from **composition**, not special cases

This mirrors real computational geometry and graphics pipelines.

---

## Results
The implementation successfully generates smooth polygonal approximations of circles
across different radii and side counts, demonstrating the correctness of the geometric model.

Example outputs include:
- low-side approximations (coarse geometry)
- high-side approximations (near-circular geometry)
- visual verification of trigonometric consistency


---

## Notes
This project emphasizes:
- abstraction over hard-coding
- mathematical reasoning over trial-and-error
- translating geometric theory into executable code

It serves as a bridge between **mathematics, computational thinking, and visualization**.

