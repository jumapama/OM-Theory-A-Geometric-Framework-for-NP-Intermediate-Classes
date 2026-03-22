"""
OM Theory: Empirical Validation Pipeline
Simulates FEM matrix assembly (Stiffness and Mass) for OM2-OM5 geometries
and runs block-Lanczos solver telemetry to evaluate spectral gaps.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import time
import json

def simulate_fem_matrices(n, family='OM2'):
    """Simulates Stiffness (K) and Mass (M) matrices for OM topologies."""
    main_diag = 2.0 * np.ones(n)
    off_diag = -1.0 * np.ones(n - 1)
    K = sp.diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csr')
    M = sp.eye(n, format='csr')
    
    # Induce topological friction (density variation) based on the OM class
    if family == 'OM2':
        K.data *= np.random.uniform(0.9, 1.1, size=K.nnz)
    elif family == 'OM3':
        K.data *= np.random.uniform(0.7, 1.3, size=K.nnz)
    elif family == 'OM4':
        K.data *= np.random.uniform(0.4, 1.6, size=K.nnz)
    elif family == 'OM5':
        K.data *= np.random.uniform(0.1, 2.0, size=K.nnz)
        K += sp.diags([np.random.uniform(0, 0.1, n)], [0])

    return K, M

def run_lanczos_solver(K, M, k_modes=10, epsilon=1e-8):
    """Executes the Krylov/Lanczos solver and tracks telemetry."""
    n = K.shape[0]
    telemetry = {"n": n, "nnz": K.nnz + M.nnz, "k": k_modes, "epsilon": epsilon}
    
    t0 = time.time()
    try:
        # Shift-and-invert to find smallest magnitude eigenvalues (spectral gap focus)
        evals, evecs = spla.eigsh(K, M=M, k=k_modes + 1, sigma=0.0, tol=epsilon)
        t_solver = time.time() - t0
        
        idx = evals.argsort()
        evals = evals[idx]
        
        # Calculate Spectral Gap and Energy
        gap = abs(evals[k_modes] - evals[k_modes-1])
        energy_topk = np.sum(evals[:k_modes]) / (np.sum(evals[:k_modes]) + gap)

        telemetry.update({
            "status": "success",
            "time_solver": t_solver,
            "gap": gap,
            "energy_topk": energy_topk
        })
    except spla.ArpackNoConvergence as e:
        telemetry.update({"status": "failed_convergence", "iterations": e.num_iterations})

    return telemetry

if __name__ == "__main__":
    print("Iniciando simulación de la Teoría OM (Lanczos/FEM)...")
    results = []
    sizes = [5000, 10000, 20000]
    
    for fam in ['OM2', 'OM3', 'OM4', 'OM5']:
        for n in sizes:
            print(f"Procesando topología {fam} con n={n}...")
            K, M = simulate_fem_matrices(n, family=fam)
            tel = run_lanczos_solver(K, M)
            tel["family"] = fam
            results.append(tel)
            
    with open('om_telemetry.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Simulación completa. Resultados guardados en om_telemetry.json.")