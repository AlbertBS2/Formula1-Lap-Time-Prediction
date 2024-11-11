# Formula 1 Lap Time Prediction 

This repository contains the solution for the [**Formula 1 Lap Time Prediction**](https://www.kaggle.com/competitions/formula-1-lap-time-prediction-nwvs-s00e02) competition, where Nick takes on a data science challenge to predict lap times for Formula One drivers. The competition involves predicting the time required for drivers to complete laps on various circuits based on historical race data.

The data provided spans Formula One races from 1996 to 2023, with the goal to predict lap times for various drivers, using features such as race details, driver stats, and circuit information.

## Overview

In this competition, participants are tasked with predicting the lap time for each driver in the test set. The evaluation metric for submissions is **Root Mean Square Error (RMSE)**.

## Dataset Description

The provided datasets cover Formula One races from 1996 through 2023. The goal is to predict the time required for drivers to complete laps on various circuits. Each row represents an individual lap by a driver, with columns providing descriptive features.

### Files provided
- **train.csv**: The training set containing historical lap data for model training.
- **test.csv**: The test set used for predictions, where the goal is to predict lap times.
- **sample_submission.csv**: A sample submission file formatted in the correct way for competition submission.

### Columns in the Dataset
- **id**: Unique identifier for the driver and lap
- **race**: Name of the race
- **date**: Date of the race (yyyy-mm-dd)
- **time**: Time of the race (hh:mm:ss)
- **circuit**: Name of the circuit
- **latitude**: Latitude of the circuit
- **longitude**: Longitude of the circuit
- **altitude**: Altitude of the circuit
- **driver**: Name of the driver
- **carNumber**: Car number of the driver
- **constructor**: Name of the constructor
- **avgDriverFinish**: Average finishing position of the driver
- **avgConstructorFinish**: Average finishing position of the constructor
- **lapNumber**: Lap number of the race
- **lapPosition**: Position of the driver during the lap
- **pitStop**: Whether there was a pit stop (1 = yes, 0 = no)
- **pitCount**: Cumulative count of the driver's pit stops during the race
- **pitTime_ms**: Time of the pit stop (in milliseconds)
- **lapTime_ms**: Time of the lap (in milliseconds) - **Target Variable**

## Submission Format

To submit predictions, the submission file should contain two columns:
1. **id**: The unique identifier for each driver lap.
2. **lapTime_ms**: The predicted lap time in milliseconds.

## Citation
DataLab351. Formula 1 Lap Time Prediction - NWVS s00e02. https://kaggle.com/competitions/formula-1-lap-time-prediction-nwvs-s00e02, 2024. Kaggle.
