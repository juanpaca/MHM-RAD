# Multiscale Hybrid-Mixed (MHM) Method – Edge-Based Implementation

This repository provides an implementation of the **Multiscale Hybrid-Mixed (MHM)** method for solving **reaction–advection–diffusion** problems using **FreeFem++** (see Araya et al. (2025)).

The solver adopts a **triple-mesh strategy**, enabling independent control of:
- the global coarse mesh,
- the edge discretization (Lagrange multipliers),
- and the local subgrid resolution.

---

## 1. Mathematical Model

We consider the elliptic problem:

$$
\nabla \cdot (-\kappa \nabla u + \boldsymbol{\alpha} u) + \sigma u = f \quad \text{in } \Omega,
$$

subject to homogeneous Dirichlet boundary conditions:

$$
u = 0 \quad \text{on } \partial \Omega.
$$

The MHM formulation decomposes the domain $\Omega$ into a set of polytopal elements $K \in \mathcal{T}_H$.  
The global coupling is performed through **Lagrange multipliers** $\lambda_H$, which represent the **normal flux across the mesh skeleton**.

---

## 2. Mesh Hierarchy

The method decouples resolution scales through three independent parameters:

- **Coarse Mesh (`-cM`)**  
  Defines the global partition $\mathcal{T}_H$.

- **Edge Mesh (`-edgeM`)**  
  Controls the discretization of the edges $\partial K$, where the hybrid unknowns $\lambda_H$ are defined.

- **Submesh (`-subM`)**  
  Defines the local refinement inside each element $K$, used to solve independent local problems.

This separation is a key feature of the MHM framework, allowing efficient multiscale resolution.

---

## 3. Requirements

- **FreeFem++** (version 4.x or higher)
- Required modules:
  - `Element_P3`
  - `Element_PkEdge`
  - `iovtk`
  - `msh3`
- **Python 3.x** (for post-processing)

---

## 4. Running the Code

Execute the solver from the terminal using:

```bash
FreeFem++ MHM-RAD_edge.edp -cM 2 -edgeM 1 -subM 2
```

### Parameters:
- `-cM`: coarse mesh level  
- `-edgeM`: edge discretization level  
- `-subM`: local refinement level over the minimal mesh created from the edge discretization 

---

## 5. Visualization with ParaView

Due to the local nature of the MHM method, results are exported as **independent `.vtu` files**, one for each element $K$.

### Step 1 — Export data

Make sure the following flag is enabled in the script:

```cpp
exportVTKlocal = true;
```

After execution, a directory (e.g., `MHMGal-EdgePartition-cM0-edgeM1-subM1-L1K3/paraview-uHh-cM0-edgeM1-L1K3`) will be created containing files like:

```
uh-0-cM0-eM1.vtu
uh-1-cM0-eM1.vtu
...
```

---

### Step 2 — Merge local solutions

To visualize the global solution as a single mesh:

1. Navigate to the results directory:
   ```
   paraview-uHh-cMx-edgeMx-LxKx
   ```
2. Place the script `singleMesh.py` inside this folder.
3. Run:

```bash
python3 singleMesh.py
```

This will generate a unified dataset for visualization in **ParaView** called `solution_uHh.pvd`.

---

## 6. About the Project

This code was developed as part of the research activities of the  
**IPES Research Group (Innovative Parallel numErical Solvers)**.

More information:  
http://ipes.lncc.br/

---

## 7. Contact

For questions or issues, please contact:

**juanpaca@posgrad.lncc.br**

## 8. References

ARAYA, Rodolfo et al. Generalizing the multiscale hybrid-mixed method for reactive-advective-diffusive equations. Computer Methods in Applied Mechanics and Engineering, v. 428, p. 117089, 2024.
