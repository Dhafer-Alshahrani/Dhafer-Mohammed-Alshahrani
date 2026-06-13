"""
                                                             SEMI-SAUDI NATIONAL SYSTEM  (S.S.N.S.)
"""
owner_of_the_project = "Dhafer Alshahrani"
group_number=4
by_teacher="Ahmed Al-hadari"
CURRENCY = "SAR"
class InSaudi:
    def __init__(self, id , name, last_name, natio,
                 dob, pob, iin_saudi=True):
        self.id = id      
        self.name = name
        self.last_name = last_name
        self.nationality = natio
        self.dob = dob                       
        self.pob = pob                       
        self.inside_saudi = iin_saudi
        self._health_record = []            
        self.__banking_info = {}  # very dangarous to share so it is private           
        self._gov_payments = []              
        self.__family_tree = {"father": [], "mother": [], "children": []} 

    def status(self):
        return f"need to add info"
    
    def iin_saudi(self):
        return self.iin_saudi
    
    def full_name(self):
        return f"{self.name} {self.last_name}"

    def presence(self, iinside):
        self.iin_saudi = iinside

    def health_notes(self, note):
        self._health_record.append(note)

    def show_health_record(self):
        return self._health_record

    def make_bank_account(self, bank_name, account_no):
        self.__banking_info[bank_name] = account_no

    def get_banking_info(self):
        return self.__banking_info
    
    def add_gov_payment(self, description, amount):
        self._gov_payments.append((description, amount)) 

    def show_gov_payments(self):
        return self._gov_payments
    
    def family_tree(self, father=None, mother=None, children=None):
        if father is not None:
            self.__family_tree["father"] = father
        if mother is not None:
            self.__family_tree["mother"] = mother
        if children is not None:
            self.__family_tree["children"] = children

    def show_family_tree(self):
        return self.__family_tree
    
    def show_all(self):
        presence = "Inside Saudi Arabia" if self.inside_saudi else "Outside KSA"
        print(f"({self.status()}) , {self.full_name()} \n ID: {self.id} , Nationality: {self.nationality} \nDate Of Birth: {self.dob} , Place Of Birth: {self.pob} , the person is  {presence}")
    
class SaudiPerson(InSaudi):

    def status(self):
        return f"Saudi Citizen"

class NonSaudiPerson(InSaudi):
    def __init__(self,id, name, last_name, natio,
                 dob, pob, iin_saudi=True, sponsor=None,
                 iqama_end=None):
        super().__init__(id, name, last_name, natio,
                          dob, pob, iin_saudi)
        self.sponsor = sponsor              
        self.iqama_end = iqama_end   

    def status(self):
        return f"Non-Saudi Resident"

    def show_all(self):
        super().show_all()

        print(f"Sponsor: {self.sponsor} \n Iqama Expiry: {self.iqama_end}")

class NewPerson(InSaudi):
    def __init__(self, id, name, last_name, natio,
                 dob, pob, iin_saudi=True):
        super().__init__(id, name, last_name, natio,
                          dob, pob, iin_saudi)

    def status(self):
        return f" New Registration"

    def show_all(self):
        super().show_all()
        print(f"Status: {self.status()}")

class DeadPerson(InSaudi):
    def __init__(self, id, name, last_name, natio,
                 dob, pob, DOD):
        super().__init__(id, name, last_name, natio,
                          dob, pob, iin_saudi=False)
        self.date_of_death = DOD

    def status(self):
        return f"The info of this body has been addded to archive (Archived)"

    def show_all(self):
        super().show_all()
        print(f"Date of Death: {self.date_of_death}")
    

class NationalRegistry:

    def __init__(self):
        self.records = {}          
        self.nationalities = set()  

def register_person(registry):
    print("\n--- Register a New Record ---")

    id = input("National ID or Iqama number: ")
    if id in registry.records:
        print("Error: a record with this ID already exists.")
        return

    name = input("First name: ")
    last_name = input("Last name: ")
    natio = input("Nationality: ")
    dob = input("Date of birth (YYYY-MM-DD): ")
    pob = input("Place of birth: ")

    x = input("THE FIELD OF THIS APPLICATION (saudi / non-saudi / new / dead): ").lower()

    try:
        match x:
            case "saudi":
                person = SaudiPerson(id, name, last_name,
                                      natio, dob, pob, True)
                print("Saudi citizen record created.")

            case "non-saudi":
                sponsor = input("Sponsor / employer: ")
                ends = input("Iqama expiry date (YYYY-MM-DD): ")
                person = NonSaudiPerson(id, name, last_name,
                                        natio, dob, pob, True,
                                         sponsor, ends)
                print("Non-Saudi resident record created.")

            case "new":
                person = NewPerson(id, name, last_name,
                                    natio,dob, pob, True)
                print("New registration created (pending finalization).")

            case "dead":
                DOD = input("Date of death (YYYY-MM-DD): ")
                person = DeadPerson(id, name, last_name,
                                     natio, dob, pob, DOD)
                print("dead person is now recorded")

            case _:
                print("Error: invalid :")
                return

    except Exception as e:
        print(f"Error while creating record: {e}")
        return

    registry.records[id] = person
    registry.nationalities.add(natio)
    person.show_all()


def check_presence(registry):
    print("\n--- Check Presence (Inside/Outside KSA) ---")
    id = input("National ID: ")

    if id not in registry.records:
        print("Error: no record found with this ID.")
        return

    person = registry.records[id]

    if person.iin_saudi:
        print(f"{person.full_name()} is currently INSIDE Saudi Arabia.")
    else:
        print(f"{person.full_name()} is currently OUTSIDE Saudi Arabia ")
        

def update_health_record(registry):
    print("\n--- Update Health Record ---")
    id = input("National ID: ")

    if id not in registry.records:
        print("Error: no record found with this ID.")
        return

    person = registry.records[id]
    note = input("Health note to add (condition,diagnoses or vacation): ")
    person.health_notes(note)

    print("Health record updated.")
    print("Current health records:", person.show_health_record())


def update_banking_info(registry):
    print("\n--- update Banking Information ---")
    id = input("National ID: ")

    if id not in registry.records:
        print("Error: no record found with this ID.")
        return

    person = registry.records[id]
    bank_name = input("Bank name: ")
    account_no = input("Account number / IBAN: ")
    person.make_bank_account(bank_name, account_no)

    print("Banking information updated.")
    print("Banking info:", person.get_banking_info())


def add_gov_payment(registry):
    print("\n--- The Government Payment ---")
    id = input("National ID: ")

    if id not in registry.records:
        print("Error: no record found with this ID.")
        return

    person = registry.records[id]
    description = input(f"( penalty , tax , loan ): ")

    try:
        amount = int(input("Amount in (SAR): "))
    except ValueError:
        print("Error: amount must be a number.")
        return

    person.add_gov_payment(description, amount)

    print("Government payment recorded.")
    print(f"All payments: {person.show_gov_payments()} {(CURRENCY)}  ")


def family_tree(registry):
    print("\n--- MAKE YOUR FAMILY TREE ---")
    id = input("National ID: ")

    if id not in registry.records:
        print("Error: no record found with this ID.")
        return

    person = registry.records[id]

    father_input = input("Father's name : ")
    mother_input = input("Mother's name : ")
    children_input = input("Children name : ")

    fathers = [f for f in father_input.split(",")] if father_input else None # here i used a new way to show the data , which is the list comprehensive and Short condition
    mothers = [m for m in mother_input.split(",")] if mother_input else None
    children = [c for c in children_input.split(",")] if children_input else None

    person.family_tree(father=fathers, mother=mothers, children=children)

    print("Family tree has been created")
    print("Family tree:", person.show_family_tree())


def search_person(registry):
    print("\n--- Search by Name ---")
    name1 = input("Enter a name to check: ").lower()

    check = False
    for person in registry.records.values():
        if name1 in person.name.lower() or name1 in person.last_name.lower():
            person.show_all()
            check = True

    if not check:
        print("No matching records found.")

def view_record(registry):
    print("\n--- View Record ---")
    id = input("National ID: ")

    if id not in registry.records:
        print("Error: no record found with this ID.")
        return

    person = registry.records[id]
    person.show_all()
    print(f"Full name: {person.full_name()}")
    print(f"Status: {person.status()}")
    print(f"Health records: {person.show_health_record()}")
    print(f"Bank info: {person.get_banking_info()}")
    print(f"Government payments: {person.show_gov_payments()}")
    print(f"Family tree: {person.show_family_tree()}")


def show_statistics(registry):
    print("\n--- System Statistics ---")

    total_records = len(registry.records)
    inside_count = sum(1 for p in registry.records.values() if p.iin_saudi())
    outside_count = total_records - inside_count

    all_status = {}
    total_payments = 0.0

    for person in registry.records.values():
        one = person.status()
        all_status[one] = all_status.get(one, 0) + 1 # get here is way to make sure that the program won't crash

        for _description, amount in person.show_gov_payments():  # unpacking to take something specific from the dict without the unneeded info
            total_payments += amount

    print(f"Total records: {total_records}")
    for one, count in all_status.items():
       print(f"{one}: {count}")

    print(f"Inside KSA : {inside_count}")
    print(f"Outside KSA : {outside_count}")
    print(f"Unique nationalities ({len(registry.nationalities)}")
    print(f"Total government payments issued: {total_payments:.2f} {CURRENCY}")


def delete_record(registry):
    print("\n--- Delete a Record ---")
    id = input("National ID: ")

    if id not in registry.records:
        print("Error: no record found with this ID.")
        return

    confirm = input(f"Are you sure you want to delete record {id}? "  # This is to agree the he wants to delete the record for ever 
                     "(yes/no): ").lower()

    match confirm:
        case "yes":
            del registry.records[id]
            print("Record deleted")
        case _:
            print("The deletion has been cancelled.")


def main():
    """
    This is the main func that gather all the fucntions to work as somth and professional as possible
    """
    registry = NationalRegistry()

    print("=" * 50)
    print("SEMI-SAUDI NATIONAL SYSTEM  (S.S.N.S.)")
    print(f"SYSTEM ADMINISTRATOR : {owner_of_the_project}")
    print("=" * 50)

    while True:
        print("-" * 50)
        print("\n  1. REGISTER PERSON ")
        print("\n  2. CHECK FAMILY TREES ")
        print("\n  3. CHECK PRESENCE (inside/outside KSA) ")
        print("\n  4. HEALTH RECORD ")
        print("\n  5. BANK INFORMATIONS ")
        print("\n  6. GOVERNMENT PAYMENTS ")
        print("\n  7. SEARCH FOR PERSON ")
        print("\n  8. VIEW A RECORD ")
        print("\n  9. DELETE A RECORD ")
        print("\n 10. SYSTEM STATISTICS ")
        print("\n 11. EXIT ")
        print("-" * 50)

        d = input("\n What is your choice:  ").strip()

        try:
            match d:
                case "1":
                    register_person(registry)
                case "2":
                    family_tree(registry)
                case "3":
                    check_presence(registry)
                case "4":
                    update_health_record(registry)
                case "5":
                    update_banking_info(registry)
                case "6":
                    add_gov_payment(registry)
                case "7":
                    search_person(registry)
                case "8":
                    view_record(registry)
                case "9":
                    delete_record(registry)
                case "10":
                    show_statistics(registry)
                case "11":
                    print("\n S.S.N.S says Goodbye, Eng.Dhafer.")
                    break
                case _:
                    print("Invalid choice, try again.")
        except Exception as e:
            print(f"Unexpected error final : {e}")
if __name__ == "__main__":
    main()
# help(main)