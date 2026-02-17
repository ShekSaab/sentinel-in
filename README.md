# SENTINEL-IN

**Supervisory Engine for Native Trading Intelligence in Listed-Equities (Indian Markets)**

A proof-of-concept policy sandbox for supervising AI-driven algorithmic trading systems, built to comply with the SEBI 2025 Algorithmic Trading Framework and RBI FREE-AI principles.


## Overview

SENTINEL-IN is a lightweight supervisory sandbox that evaluates and monitors AI trading models before they interact with live markets. It addresses the core challenge of transitioning AI models from unregulated "black boxes" to governed, explainable financial instruments.

### Key Capabilities

- **Drift Detection** — Real-time monitoring of model decay using Population Stability Index (PSI) and Kolmogorov-Smirnov tests
- **Pre-Trade Risk Controls** — SEBI Annexure 5 compliant validation (price bands, order throttle, position limits)
- **Policy Engine** — Tiered trade validation: auto-approve, committee review, or human oversight


## Technology Stack

- **Python 3.11.9**
- **NumPy / Pandas / Scikit-learn** — Data processing and ML
- **SciPy** — Statistical tests (K-S test)
- **Matplotlib / Seaborn** — Visualisations
- **Pytest** — Testing


## Motivation

I am developing this project as a practical implementation of supervisory technology (SupTech) for AI-driven trading, addressing the regulatory requirements introduced by SEBI's 2025 circular on algorithmic trading and the RBI's FREE-AI framework. It demonstrates the intersection of computational finance, machine learning governance, and regulatory compliance.
