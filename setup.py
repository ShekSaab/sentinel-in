from setuptools import setup, find_packages

setup(
    name="sentinel-in",
    version="0.1.0",
    description="Supervisory Policy Sandbox for AI-Driven Trading Compliance",
    author="Your Name",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "scipy>=1.11.0",
        "shap>=0.42.0",
        "lime>=0.2.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.23.0",
        "pydantic>=2.0.0",
    ],
)
