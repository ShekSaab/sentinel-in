# SEBI 2025 Compliance Mapping

This document maps SENTINEL-IN's modules to the specific requirements
of SEBI's 2025 Algorithmic Trading Framework and the RBI FREE-AI principles.

---

## SEBI 2025 Circular: Algorithmic Trading Framework

### Strategy Categorisation

SEBI requires all algorithmic strategies to be classified as either
**White Box** (transparent logic) or **Black Box** (proprietary/hidden logic).
Black Box providers must maintain detailed research reports explaining the
underlying rationale.

**SENTINEL-IN Module**: XAI Explainer (`sentinel_in/xai/explainer.py`)

The XAI module generates automated interpretability reports using SHAP (global)
and LIME (local) that meet the research report documentation requirements
for Black Box strategies.

### Pre-Trade Risk Controls (Annexure 5)

All algorithmic orders must pass through automated Risk Management Systems
before execution.

**SENTINEL-IN Module**: Risk Controls (`sentinel_in/risk/controls.py`)

Implements the full Annexure 5 suite: Limit Price Protection (Sr. 4),
Market Price Protection (Sr. 5), Cumulative Open Order Value (Sr. 6),
Margin and Position Checks (Sr. 7 & 10), Regulatory Blocklists (Sr. 8 & 9),
and Order Throttle Limits (10 OPS).

### Continuous Monitoring

Strategies must be monitored for performance degradation with circuit
breaker mechanisms for emergency situations.

**SENTINEL-IN Module**: Drift Monitor (`sentinel_in/drift/monitor.py`)

Implements PSI and K-S test based drift detection with three-tier alerting
(GREEN/AMBER/RED) and automatic circuit breaker activation.

### Kill Switch Requirement

Brokers must maintain emergency kill switch capability to halt all
algorithmic trading instantly.

**SENTINEL-IN Module**: Stress Engine (`sentinel_in/stress/scenarios.py`)

The kill switch activates automatically when portfolio drawdown exceeds
the configured threshold (default: 15%).

---

## RBI FREE-AI Framework Alignment

| FREE-AI Sutra | Principle | SENTINEL-IN Implementation |
|---|---|---|
| Sutra 1 | Fairness | Blocklist enforcement for restricted instruments |
| Sutra 2 | Transparency | SHAP/LIME explainability reports |
| Sutra 3 | Accountability | Full audit trail in validation log |
| Sutra 4 | Reliability | Drift detection and circuit breakers |
| Sutra 5 | Security | Tiered validation (auto/committee/human) |
| Sutra 6 | Efficiency | Automated pre-trade checks at 10 OPS |
| Sutra 7 | Ethics | Position limits and cumulative value caps |
