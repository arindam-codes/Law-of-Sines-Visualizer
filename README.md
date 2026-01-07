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



![IMG_20251208_071443](https://github.com/user-attachments/assets/6156874e-c3e9-44da-b189-9de9ab1f49eb)

i generelized the isosceles triangle the base as sin(fi) / ( radius of the circle * sin(theta) )
  where theta is angle btw adjacent sides 
  and fi is the rest two angle os the isosceles triangle 

so finally the outputs i got is 

![Screenshot_from_2025-12-08_07-08-03](https://github.com/user-attachments/assets/554bfad5-50d1-4edc-b8cc-094a90faefd9)

![Screenshot_from_2025-12-08_07-08-36](https://github.com/user-attachments/assets/2b9311aa-55d8-4fdf-a847-3ea3fbe8dcfd)

![IMG_20251208_071426](https://github.com/user-attachments/assets/46a5bf6c-fce9-4a82-b035-dd5d16d5a548)
