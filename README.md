# IDX30 PCA Portfolio Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-yellowgreen)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4%2B-green)
![yFinance](https://img.shields.io/badge/yFinance-0.2%2B-lightgrey)

This repository contains the implementation and analysis of portfolio management and risk assessment for IDX30 stocks using Principal Component Analysis (PCA). The project leverages Python and its libraries to uncover risk factors, assess stock contributions, and construct optimized portfolios.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Results](#results)

---

## Introduction

This project explores the effectiveness of PCA in identifying systematic and idiosyncratic risks in IDX30 stocks. By analyzing principal components, this study aims to:
- Uncover key risk factors affecting portfolio performance.
- Construct portfolios with varying risk and return profiles.
- Compare portfolio performances based on different PCA-driven weightings.

The research highlights PCA as a tool for risk management and diversification while emphasizing its limitations in guaranteeing superior returns.

---

## Features

- **PCA Implementation:** Perform PCA on IDX30 stock returns to extract principal components and explained variance.
- **Portfolio Construction:** Create portfolios using:
  - Top principal components (PC1, Top 3 PCs, etc.)
  - 95% variance portfolio
  - Equal weight portfolio
  - Custom weight portfolio
- **Risk Analysis:** Assess stock loadings and their contributions to systematic and specific risks.
- **Visualization:** Generate graphs for cumulative returns, explained variance, stock loadings, and portfolio weights.

---

## Project Structure

```plaintext
📂 IDX30-PCA-Portfolio-Analysis/
├── docs/                        # Documentation related to the project
├── img/                         # Folder containing generated visualizations and plots
├── src/                         # Source code folder containing Python scripts
│   ├── main.py                  # Main script to execute the PCA-based portfolio analysis
│   ├── pca.py                   # PCA implementation and related utility functions
│   ├── data_preprocessing.py    # Functions for fetching and preprocessing IDX30 stock data
│   ├── quantitative_analysis.py # Functions for calculating portfolio performance metrics
│   └── visualizations.py        # Functions for generating charts and visual insights
├── LICENSE                      # License information for the project
├── README.md                    # Detailed project overview and setup instructions
└── requirements.txt             # List of Python libraries and dependencies required for the project


```

---

## Setup and Installation

Follow these steps to set up and run the project:

### Prerequisites
Ensure you have Python 3.8 or higher installed. You can check your version by running:
```bash
python --version
```
### Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/0xNathaniel/IDX30-PCA-Analysis.git
cd IDX30-PCA-Analysis
```
### Install Dependencies
Install the required Python libraries using the requirements.txt file:
```bash
pip install -r requirements.txt
```

### Usage
Run the following command to execute the main script:
```bash
cd src
python main.py
```

---

## Results
- **Key Insights**
  - Portfolios constructed with broader principal components exhibited better diversification and risk mitigation.
  - Custom weight portfolios demonstrated the potential for superior returns when aligned with strategic investment goals.
- **Limitations**
  - PCA alone does not guarantee superior performance; combining it with economic and strategic factors is recommended.