import json
import os
from datetime import datetime


# =========================================================
# VEDA TECHNOLOGY BUSINESS & SERVICE MANAGEMENT SYSTEM
# =========================================================

DATA_FILE = "veda_data.json"


# ---------------------------------------------------------
# Default Data
# ---------------------------------------------------------

DEFAULT_DATA = {
    "technology_programs": [],
    "digital_services": [],
    "training_programs": [],
    "internship_programs": [],
    "customer_inquiries": [],
    "service_requests": []
}


# ---------------------------------------------------------
# Utility Functions
# ---------------------------------------------------------

def load_data():
    """Load data from JSON file."""

    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DATA.copy())
        return DEFAULT_DATA.copy()

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        print("Data file is invalid. Creating a new database.")
        save_data(DEFAULT_DATA.copy())
        return DEFAULT_DATA.copy()


def save_data(data):
    """Save data into JSON file."""

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def generate_id(items, prefix):
    """Generate unique ID."""

    if not items:
        return f"{prefix}001"

    numbers = []

    for item in items:
        try:
            number = int(item["id"].replace(prefix, ""))
            numbers.append(number)
        except ValueError:
            pass

    next_number = max(numbers, default=0) + 1

    return f"{prefix}{next_number:03d}"


def get_required_input(message):
    """Validate required input."""

    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def display_records(records):
    """Display records."""

    if not records:
        print("\nNo records found.")
        return

    print("\n" + "=" * 70)

    for record in records:
        print("=" * 70)

        for key, value in record.items():
            print(f"{key.title():20}: {value}")

    print("=" * 70)


# ---------------------------------------------------------
# Main Management Class
# ---------------------------------------------------------

class VedaManagementSystem:

    def __init__(self):
        self.data = load_data()

    def save(self):
        save_data(self.data)

    # =====================================================
    # TECHNOLOGY PROGRAMS
    # =====================================================

    def add_technology_program(self):

        print("\n--- Add Technology Program ---")

        program = {
            "id": generate_id(
                self.data["technology_programs"],
                "TP"
            ),
            "name": get_required_input("Program name: "),
            "department": get_required_input("Department: "),
            "duration": get_required_input("Duration: "),
            "status": "Active",
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }

        self.data["technology_programs"].append(program)
        self.save()

        print("\nTechnology program added successfully!")
        print("Program ID:", program["id"])

    def view_technology_programs(self):

        print("\n--- Technology Programs ---")

        display_records(
            self.data["technology_programs"]
        )

    # =====================================================
    # DIGITAL SERVICES
    # =====================================================

    def add_digital_service(self):

        print("\n--- Add Digital Service ---")

        service = {
            "id": generate_id(
                self.data["digital_services"],
                "DS"
            ),
            "name": get_required_input("Service name: "),
            "category": get_required_input("Category: "),
            "description": get_required_input("Description: "),
            "status": "Available"
        }

        self.data["digital_services"].append(service)
        self.save()

        print("\nDigital service added successfully!")
        print("Service ID:", service["id"])

    def view_digital_services(self):

        print("\n--- Digital Services ---")

        display_records(
            self.data["digital_services"]
        )

    # =====================================================
    # TRAINING PROGRAMS
    # =====================================================

    def add_training_program(self):

        print("\n--- Add Training Program ---")

        training = {
            "id": generate_id(
                self.data["training_programs"],
                "TR"
            ),
            "name": get_required_input("Training name: "),
            "technology": get_required_input("Technology: "),
            "duration": get_required_input("Duration: "),
            "mode": get_required_input(
                "Mode (Online/Offline): "
            ),
            "status": "Open"
        }

        self.data["training_programs"].append(training)
        self.save()

        print("\nTraining program added successfully!")
        print("Training ID:", training["id"])

    def view_training_programs(self):

        print("\n--- Training Programs ---")

        display_records(
            self.data["training_programs"]
        )

    # =====================================================
    # INTERNSHIP PROGRAMS
    # =====================================================

    def add_internship(self):

        print("\n--- Add Internship Program ---")

        internship = {
            "id": generate_id(
                self.data["internship_programs"],
                "IN"
            ),
            "title": get_required_input("Internship title: "),
            "technology": get_required_input("Technology: "),
            "duration": get_required_input("Duration: "),
            "stipend": get_required_input(
                "Stipend: "
            ),
            "status": "Open"
        }

        self.data["internship_programs"].append(internship)
        self.save()

        print("\nInternship program added successfully!")
        print("Internship ID:", internship["id"])

    def view_internships(self):

        print("\n--- Internship Programs ---")

        display_records(
            self.data["internship_programs"]
        )

    # =====================================================
    # CUSTOMER INQUIRIES
    # =====================================================

    def add_customer_inquiry(self):

        print("\n--- Customer Inquiry ---")

        inquiry = {
            "id": generate_id(
                self.data["customer_inquiries"],
                "CI"
            ),
            "customer_name": get_required_input(
                "Customer name: "
            ),
            "email": get_required_input(
                "Email: "
            ),
            "subject": get_required_input(
                "Subject: "
            ),
            "message": get_required_input(
                "Message: "
            ),
            "status": "Pending",
            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        }

        self.data["customer_inquiries"].append(inquiry)
        self.save()

        print("\nCustomer inquiry submitted successfully!")
        print("Inquiry ID:", inquiry["id"])

    def view_inquiries(self):

        print("\n--- Customer Inquiries ---")

        display_records(
            self.data["customer_inquiries"]
        )

    # =====================================================
    # SERVICE REQUESTS
    # =====================================================

    def add_service_request(self):

        print("\n--- Service Request ---")

        request = {
            "id": generate_id(
                self.data["service_requests"],
                "SR"
            ),
            "customer_name": get_required_input(
                "Customer name: "
            ),
            "service": get_required_input(
                "Service required: "
            ),
            "description": get_required_input(
                "Problem description: "
            ),
            "priority": get_required_input(
                "Priority (Low/Medium/High): "
            ),
            "status": "Open",
            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        }

        self.data["service_requests"].append(request)
        self.save()

        print("\nService request created successfully!")
        print("Request ID:", request["id"])

    def view_service_requests(self):

        print("\n--- Service Requests ---")

        display_records(
            self.data["service_requests"]
        )

    # =====================================================
    # REPORT
    # =====================================================

    def generate_report(self):

        print("\n")
        print("=" * 60)
        print("        VEDA TECHNOLOGY BUSINESS REPORT")
        print("=" * 60)

        print(
            f"Technology Programs : "
            f"{len(self.data['technology_programs'])}"
        )

        print(
            f"Digital Services    : "
            f"{len(self.data['digital_services'])}"
        )

        print(
            f"Training Programs   : "
            f"{len(self.data['training_programs'])}"
        )

        print(
            f"Internship Programs : "
            f"{len(self.data['internship_programs'])}"
        )

        print(
            f"Customer Inquiries  : "
            f"{len(self.data['customer_inquiries'])}"
        )

        print(
            f"Service Requests    : "
            f"{len(self.data['service_requests'])}"
        )

        # Count pending inquiries
        pending_inquiries = sum(
            1
            for item in self.data["customer_inquiries"]
            if item["status"] == "Pending"
        )

        # Count open requests
        open_requests = sum(
            1
            for item in self.data["service_requests"]
            if item["status"] == "Open"
        )

        print("-" * 60)

        print(
            f"Pending Inquiries   : {pending_inquiries}"
        )

        print(
            f"Open Service Requests: {open_requests}"
        )

        print("=" * 60)

    # =====================================================
    # SEARCH
    # =====================================================

    def search(self):

        keyword = get_required_input(
            "\nEnter search keyword: "
        ).lower()

        results = []

        for category, records in self.data.items():

            for record in records:

                record_text = json.dumps(
                    record
                ).lower()

                if keyword in record_text:

                    results.append(
                        {
                            "category": category,
                            **record
                        }
                    )

        print("\n--- Search Results ---")

        display_records(results)


# ---------------------------------------------------------
# Menu
# ---------------------------------------------------------

def show_menu():

    print("\n")
    print("=" * 60)
    print("       VEDA TECHNOLOGY MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1.  Add Technology Program")
    print("2.  View Technology Programs")

    print("3.  Add Digital Service")
    print("4.  View Digital Services")

    print("5.  Add Training Program")
    print("6.  View Training Programs")

    print("7.  Add Internship Program")
    print("8.  View Internship Programs")

    print("9.  Add Customer Inquiry")
    print("10. View Customer Inquiries")

    print("11. Add Service Request")
    print("12. View Service Requests")

    print("13. Search Records")
    print("14. Generate Business Report")

    print("0.  Exit")

    print("=" * 60)


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    system = VedaManagementSystem()

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":
            system.add_technology_program()

        elif choice == "2":
            system.view_technology_programs()

        elif choice == "3":
            system.add_digital_service()

        elif choice == "4":
            system.view_digital_services()

        elif choice == "5":
            system.add_training_program()

        elif choice == "6":
            system.view_training_programs()

        elif choice == "7":
            system.add_internship()

        elif choice == "8":
            system.view_internships()

        elif choice == "9":
            system.add_customer_inquiry()

        elif choice == "10":
            system.view_inquiries()

        elif choice == "11":
            system.add_service_request()

        elif choice == "12":
            system.view_service_requests()

        elif choice == "13":
            system.search()

        elif choice == "14":
            system.generate_report()

        elif choice == "0":
            print("\nThank you for using Veda Technology System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# ---------------------------------------------------------
# Program Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()