
import pandas as pd
import numpy as np
from functions import calculate_average, assign_result, find_topper

print("=" * 45)
print(" STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 45)

try:
    # Load CSV Dataset
    df = pd.read_csv("students.csv")

    if df.empty:
        raise ValueError("students.csv is empty!")

    # Required columns check
    required_columns = [
        "Student_ID", "Name", "Department",
        "Python", "Math", "English", "Attendance"
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # Calculate Average, Total, Grade and Result
    df = calculate_average(df)
    df = assign_result(df)

    subjects = ["Python", "Math", "English"]

    # Student Data
    print("\nSTUDENT DATA:")
    print(df.to_string(index=False))

    # Dataset Summary
    print("\nDATASET SUMMARY:")
    print("Total Students:", len(df))
    print("Total Subjects:", len(subjects))

    # Dataset Statistics
    print("\nDATASET STATISTICS:")
    print(df[subjects + ["Attendance"]].describe().round(2))

    # NumPy Calculation
    all_marks = df[subjects].to_numpy()
    overall_average = np.mean(all_marks)

    print("\nOVERALL CLASS AVERAGE:")
    print(round(overall_average, 2))

    # Subject-wise Performance Analysis
    print("\nSUBJECT-WISE AVERAGE:")
    for subject in subjects:
        subject_average = np.mean(df[subject].to_numpy())
        print(subject, "Average:", round(subject_average, 2))

    # Class Topper
    topper = find_topper(df)

    print("\nCLASS TOPPER:")
    print("Name:", topper["Name"])
    print("Average Marks:", topper["Average"])

    # Highest and Lowest Performance
    highest = df.loc[df["Average"].idxmax()]
    lowest = df.loc[df["Average"].idxmin()]

    print("\nHIGHEST PERFORMANCE:")
    print("Name:", highest["Name"])
    print("Average Marks:", highest["Average"])

    print("\nLOWEST PERFORMANCE:")
    print("Name:", lowest["Name"])
    print("Average Marks:", lowest["Average"])

    # Top 3 Performing Students
    print("\nTOP 3 PERFORMING STUDENTS:")
    top_students = df.sort_values(
        by="Average", ascending=False
    ).head(3)

    print(top_students[["Name", "Average", "Grade"]].to_string(index=False))

    # Result Summary
    print("\nRESULT SUMMARY:")
    print(df["Result"].value_counts().to_string())

    # Pass/Fail Summary
    print("\nPASS/FAIL SUMMARY:")
    print("Total Passed:", (df["Result"] == "Pass").sum())
    print("Total Failed:", (df["Result"] == "Fail").sum())

    # Save Final Report
    df.to_csv("student_analysis_report.csv", index=False)
    print("\nReport saved: student_analysis_report.csv")

except FileNotFoundError:
    print("Error: students.csv file not found!")

except pd.errors.EmptyDataError:
    print("Error: students.csv is empty!")

except Exception as e:
    print("Error:", e)
