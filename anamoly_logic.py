from data_store import data


# Add data
def add_data():
    value = float(input("Enter a value: "))
    data.append(value)
    print("Value added successfully!")


# Show data
def show_data():
    print("Current Data:", data)


# Detect anomaly
def detect_anomaly():
    if len(data) == 0:
        print("No data available!")
        return

    avg = sum(data) / len(data)

    print("Average value:", avg)

    print("\nAnomalies:")
    found = False

    for x in data:
        if x > avg * 1.5 or x < avg * 0.5:
            print(x)
            found = True

    if not found:
        print("No anomalies detected.")