import anomaly_logic

while True:
    print("\n===== AI ANOMALY DETECTION MENU =====")
    print("1. Add Data")
    print("2. Show Data")
    print("3. Detect Anomaly")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        anomaly_logic.add_data()

    elif choice == "2":
        anomaly_logic.show_data()

    elif choice == "3":
        anomaly_logic.detect_anomaly()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")