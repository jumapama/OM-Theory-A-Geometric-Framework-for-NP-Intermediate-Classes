# OM Theory: A Geometric Framework for NP-Intermediate Classes

Hi everyone,

I've been working on a theoretical computer science framework that attempts to map computational complexity—specifically the boundary between $\mathsf{P}$, $\mathsf{NP}$, and $\mathsf{NP}$-Intermediate classes like Integer Factorization—into a purely geometric and topological problem. I call it **Frame Orientation Theory (OM Theory)**.

Instead of treating problems like SAT or Factorization as pure combinatorial searches, OM Theory maps problem instances into a topological space (metaphorically, a "Cube"). The complexity of a problem is defined by the *density of certificates* when the instance is projected onto different mathematical "frames" (the faces of the cube).

I am publishing this here to invite brutal, rigorous peer review from the theoretical computer science, cryptography, and algorithm engineering communities.

## Core Concepts of the Framework

1. **The OM Classes (The Geometry of Complexity):**
   * **OM-1 ($\mathsf{NP}$-Complete):** The hypercube surface. A topology with exponential density $\Theta(2^n)$ and severe bottlenecks (poor Cheeger constant).
   * **OM-6 ($\mathsf{P}$):** The native spherical topology. Polynomial density, where algorithms can flow smoothly to the solution in $O(\text{poly})$.
   * **The $\mathcal{I}$ Belt ($\mathsf{NP}$-Intermediate):** This is where Integer Factorization lives (OM-2 to OM-5). The theory models this as an intermediate topological regime with a certificate density of $\Theta(n^K \log n)$. 

2. **Spectral Distinguishability ($d_{\mathrm{spec}}$):**
   To prevent trivial Karp reductions (like adding syntactic tautologies to pad an instance), the framework introduces a strict metric based on the Laplacian spectrum of the problem's mesh. Two frames are only valid if they are topologically non-homotopic and demonstrate a measurable spectral gap difference.

<img width="4200" height="1800" alt="analisis_om_resultados" src="https://github.com/user-attachments/assets/e9380980-6d00-4aed-a18f-d320038ea112" />

3. **Axiom 7 (Asymptotic Density Stability):**
   A new axiomatic rule to prevent Ladner's theorem "padding" tricks. It mathematically forces the density of a class to remain asymptotically stable, preventing artificial oscillations between $\mathsf{P}$ and $\mathsf{NP}$ across input sizes.

4. **The $OM\text{-}k$ Decision Problem:**
   I have included a proof demonstrating that deciding whether an instance can be successfully projected onto $k$ distinct, spectrally valid frames is, conditionally, an $\mathsf{NP}$-Complete problem.

5. **The "Caterpillar" Heuristic:**
   An algorithmic approach to navigate the $\mathcal{I}$ belt. It uses block-Lanczos algorithms over $\mathbb{GF}(2)$ and Finite Element Method (FEM) remeshing to track the spectral gap and find the correct frame orientation.

## What's in this Repository?

* **`OM_Theory_Formal_Axioms.pdf`**: The formal paper containing the axioms, the definition of spectral distinguishability, and the $\mathsf{NP}$-Completeness proof. *(Note: You need to upload your Documento D here)*
* **`om_pipeline_simulation.py`**: A Python script simulating the FEM matrix assembly (Stiffness and Mass matrices) for OM geometries, running the block-Lanczos solver, and collecting telemetry on the spectral gap as $n$ scales.
* **`om_cube_visualization.py`**: The code to render the 3D topological model of the framework.

## The Ask: Tear my axioms apart

I am sharing this because I need adversarial eyes on the math. 
* Does the $d_{\mathrm{spec}}$ formulation successfully prevent all trivial syntactic padding? 
* Does Axiom 7 hold up against classical complexity theory critiques?
* Are there counterexamples in the $\mathcal{I}$ class that break the $\Theta(n^K \log n)$ density rule?

Talk is cheap, so the code and the proofs are in the repo. I look forward to your critiques, issues, and pull requests.

Thank you.
