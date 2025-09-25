# Siemens Energy Digitalization Metrics Dashboard
# Developed Using Python by Heider Jeffer
# Refined Version

import math
from typing import List
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


# --- Metric Functions ---

# 1) Time Saved by Automation
def time_saved(T_manual: float, R: float) -> float:
    """Calculate time saved by automation."""
    return T_manual * R

# 2) ROI (Return on Investment)
def roi(C_saved: float, C_project: float) -> float:
    """Calculate ROI percentage."""
    return ((C_saved - C_project) / C_project) * 100

# 3) Data Quality Index
def data_quality(N_errors: int, N_total: int) -> float:
    """Calculate data quality index (0-1)."""
    if N_total == 0:
        return 0.0
    return 1 - (N_errors / N_total)

# 4) Anomaly Detection (Threshold Method)
def is_anomaly(x_i: float, mu: float, sigma: float, k: float) -> bool:
    """Check if a data point is an anomaly."""
    return abs(x_i - mu) > k * sigma

# 5) System Optimization
def system_optimization(P: List[float], C: List[List[float]]) -> float:
    """Aggregate system performance metrics."""
    total = sum(P)
    for row in C:
        total += sum(row)
    return total

# 6) CIA Principles (Confidentiality, Integrity, Availability)
def secure_system_index(P_conf: float, P_integrity: float, P_avail: float) -> float:
    """Compute CIA security index."""
    return P_conf * P_integrity * P_avail

# 7) KPI Aggregation
def kpi_index(weights: List[float], KPIs: List[float]) -> float:
    """Aggregate multiple KPIs using weighted average."""
    if sum(weights) == 0:
        return 0.0
    return sum(w * k for w, k in zip(weights, KPIs)) / sum(weights)

# 8) Automation Pipeline Success Probability
def pipeline_success(P_etl: float, P_rpa: float, P_report: float) -> float:
    """Calculate probability of full automation pipeline success."""
    return P_etl * P_rpa * P_report

# 9) First 90 Days Efficiency
def efficiency_over_time(t: int, E_max: float) -> float:
    """Linear efficiency growth over the first 90 days."""
    if t < 0:
        return 0.0
    t = min(t, 90)
    return E_max * (t / 90)

# 10) Scaling Factor
def total_improvement(N_sites: int, S_unit: float) -> float:
    """Compute total improvement across multiple sites."""
    return N_sites * S_unit


# --- Visualization Functions ---

def plot_efficiency(E_max=1.0):
    days =
