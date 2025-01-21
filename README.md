# Optimal Coin Expenditure for Mario Wonder Standees

This program performs Monte Carlo simulations to estimate the optimal coin expenditure strategy for collecting all 144 standees in *Mario Wonder*. The goal is to determine how many random standees should be purchased before switching to guaranteed new standees to minimize total coin usage.

## Background

There are two primary methods to obtain standees:
1. **Random Standees**: Costs 10 coins per draw but may result in duplicates.
2. **Guaranteed New Standees**: Costs 30 coins per draw and ensures no duplicates.

- Buying only random standees requires approximately **2,100 draws** to collect all 144 standees, costing a total of **21,000 coins**.
- Conversely, buying only guaranteed new standees costs **4,320 coins** to collect all standees.
- To optimize coin expenditure, we estimate the point at which switching from random to guaranteed standees becomes more cost-effective.

## Key Findings

Based on the simulations:
- **Random standees** should be purchased until your collection contains approximately **78 to 80 standees**.
- At this point, switching to **guaranteed standees** becomes financially advantageous.
- Using this strategy, the total expected expenditure is around **3,272 coins**.

## Results

Below are plots illustrating the simulation results:

### Simulation Plots

<p align="center">
  <img src="assets/Figure_1.png" alt="Figure 1: Simulation 1"/>
  <img src="assets/Figure_2.png" alt="Figure 2: Simulation 2"/>
  <img src="assets/Figure_3.png" alt="Figure 3: Simulation 3"/>
  <img src="assets/Figure_4.png" alt="Figure 4: Simulation 4"/>
</p>

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/mario-standees
   ```
2. Run the program:
   ```bash
   python simulate.py
   ```
3. Modify parameters in `simulate.py` to adjust probabilities or analyze other scenarios.

## Requirements

- Python 3.x
- Required libraries (install with `pip`):
  ```bash
  pip install numpy pandas matplotlib tqdm
  ```

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the program or expand the analysis.

Enjoy optimizing your coin expenditure in Mario Wonder!
