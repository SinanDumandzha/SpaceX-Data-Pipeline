import pandas as pd

spacex_data = {
    "rocket": [
        "Falcon 1",
        "Falcon 9",
        "Falcon Heavy",
    ],
    "launches": [5, 100, 3],
}

df = pd.DataFrame(spacex_data)

print(df)

print(df["rocket"])

most_launched_rockets = df[df["launches"] > 5]

df["success_rate"] = [0.4, 0.98, 1.0]
