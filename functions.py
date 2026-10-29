
import pandas as pd
import numpy as np


def calculate_average(df):
    subjects = ["Python", "Math", "English"]

    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = df[subjects].mean(axis=1).round(2)

    return df


def assign_result(df):
    subjects = ["Python", "Math", "English"]

    df["Result"] = df[subjects].apply(
        lambda row: "Pass" if all(mark >= 33 for mark in row) else "Fail",
        axis=1
    )

    def get_grade(avg):
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    df["Grade"] = df["Average"].apply(get_grade)

    return df


def find_topper(df):
    return df.loc[df["Average"].idxmax()]
