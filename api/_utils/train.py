import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from .save import save_model_pickle
import os

data = pd.read_csv(f"{os.path.dirname(__file__)}/data.csv")
INPUT_COLUMNS = [
    "mainFloorLengthInFt",
    "mainFloorBreadthInFt",
    "ceilingHeightInFt",
    "numberOfFloors",
    "numberOfKitchens",
    "numberOfStandaloneToilets",
    "numberOfFullBathrooms",
    "numberOfRooms",
    "priceOfBagOfCement",
    "priceOfTripOfSand",
    "priceOfWaterInLiters",
    "priceOfDoorD1",
    "priceOfDoorD2",
    "priceOfDoorD3",
    "priceOfWindowW1",
    "priceOfWindowW2",
    "priceOfTilesPerM2",
    "priceOfGraniteInTonnes",
    "priceOfSteelPerM3",
    "priceOfCostOfRoofHalfPlot",
]
X = data[INPUT_COLUMNS]

y = data[
    [
        "estimatedBlocksNeeded",
        "estimatedCementBagsNeeded",
        "estimatedConcreteNeeded",
        "estimatedCost",
        "estimatedCostOfRoofing",
        "estimatedNumDoors",
        "estimatedNumDoorsD1",
        "estimatedNumDoorsD2",
        "estimatedNumDoorsD3",
        "estimatedNumWindows",
        "estimatedNumWindowsW1",
        "estimatedNumWindowsW2",
        "estimatedPricePerConcreteInM3",
        "estimatedSandInTonnesNeeded",
        "estimatedVolumeOfSlabNeeded",
        "estimatedTripsOfSandsNeeded",
        "estimatedSteelNeeded",
    ]
]
model = RandomForestRegressor(random_state=0, max_depth=7)
model.fit(X, y)

save_model_pickle(model, f"{os.path.dirname(__file__)}/model.pickle")
