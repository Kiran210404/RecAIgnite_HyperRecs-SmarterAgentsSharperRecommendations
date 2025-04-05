import sqlite3
import pandas as pd

users_df = pd.read_csv("C:/Users/KIRAN_MANE/OneDrive/Desktop/AgenticAI/backend/GFG_Dataset/GFG_Dataset/customer_data_collection.csv")
print("User CSV Columns:", users_df.columns.tolist())  # <-- Add this to debug


#users_df = pd.read_csv("C:/Users/KIRAN_MANE/OneDrive/Desktop/AgenticAI/backend/GFG_Dataset/GFG_Dataset/customer_data_collection.csv")

#products_df = pd.read_csv("C:/Users/KIRAN_MANE/OneDrive/Desktop/AgenticAI/backend/GFG_Dataset/GFG_Dataset/product_recommendation_data.csv")

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agents.recommendation_agent import RecommendationAgent
