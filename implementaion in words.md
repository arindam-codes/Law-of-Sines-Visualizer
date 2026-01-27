
Where:
- `θ` is the angle between adjacent sides of the polygon
- `φ` is the remaining equal angle of the isosceles triangle
- `radius` is the radius of the target circle

This formulation allows the circle approximation to scale smoothly with both radius and resolution.

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
