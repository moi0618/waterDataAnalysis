from flask import Flask, jsonify
import pandas as pd


df1 = pd.read_csv("Data/2021-dec16.csv")
df2 = pd.read_csv("Data/2021-oct21.csv")
df3 = pd.read_csv("Data/2022-nov16.csv")
df4 = pd.read_csv("Data/2022-oct7.csv")

print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())
