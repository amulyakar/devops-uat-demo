import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


def main():
    # Reference data: normal baseline
    reference_data = pd.DataFrame({
        "age": [20, 21, 22, 23, 24, 25, 26, 27],
        "score": [60, 65, 70, 72, 75, 78, 80, 82]
    })

    # Current data: intentionally different values
    current_data = pd.DataFrame({
        "age": [30, 31, 32, 33, 34, 35, 36, 37],
        "score": [40, 45, 48, 50, 52, 55, 58, 60]
    })

    report = Report([DataDriftPreset()])
    snapshot = report.run(current_data, reference_data)
    snapshot.save_html("evidently_report.html")

    print("Evidently monitoring completed.")
    print("Report saved as evidently_report.html")


if __name__ == "__main__":
    main()