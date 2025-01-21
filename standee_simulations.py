import random
import numpy as np
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt


def simulate(threshold, num_simulations=1000):
    costs = []
    for _ in range(num_simulations):
        collection = set()
        total_cost = 0

        while len(collection) < 144:
            if len(collection) < threshold:
                total_cost += 10
                item = random.choices(
                    population=list(range(144)),
                    weights=[0.55 if i < 48 else 0.35 if i < 96 else 0.10 for i in range(144)]
                )[0]
            else:
                total_cost += 30
                available_items = set(range(144)) - collection
                item = random.choice(list(available_items))

            collection.add(item)

        costs.append(total_cost)

    return np.mean(costs)


if __name__ == "__main__":
    thresholds = range(72, 85, 1)
    results = {}

    for threshold in tqdm(thresholds):
        avg_cost = simulate(threshold, num_simulations=5000)
        results[threshold] = avg_cost

    results_df = pd.DataFrame(list(results.items()), columns=["Threshold", "Average Cost"])

    plt.plot(results_df["Threshold"], results_df["Average Cost"])
    plt.xlabel("Threshold")
    plt.ylabel("Average Cost")
    plt.show()
