# Predicting Cannula Distorted Defect Based On Hardness Measurement Value

## Problem Statement
Estimated RM300,000 is loss for the year 2024 due to distorted-melted problem of cannula at Cannula Production in B. Braun Medical Industries. Prediction to detect the defect above is vital to save the cost and reduce the loss and wastage. We make a hypothesis that the hardness of material can be a factor to cause distorted-melted of the cannula. The hardness study never been done before in our site. So, decision made to collect data of hardness of the material and compute a machine learning algorithm to do early prediction of the defect before it reaching Final Inspection Process.

![Distorted Sample](distorted_sample.png)

## Objective
- To find the relationship between the hardness of material and the defect of distorted-melted.
- To classify the cannula defect of distorted at early stage to reduce loss and wastage.

## Dataset
Y - Defect (Distorted or Not),
X - Input Feature (Hardness reading at Drawing, Bright Annealing, Sinking and Electro Fission)

## Production Process Flow
![Process Flow](processflow.png)
Above shows the process flow of Cannula Production. There are 4 process where the hardness measurement of the cannula have been taken that are in the red rectangle. With this project we can detect the defect earlier than current detection point thus can reduce the amount of wastage and reduce cost of reprocessing.

