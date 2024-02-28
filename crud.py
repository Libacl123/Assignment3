from utils import create, retrieve, update, delete

def main():
  
  while True:
    print("\nCRUD operations on districts are :")
    print("1. Create")
    print("2. Retrieve")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      name = input("Enter district name: ")
      create({"name": name})
    elif choice == "2":
        t_id = int(input("Enter district ID: "))
        district = retrieve(t_id)
        if district:
          print(district)
        else:
          print("District not found.")
    elif choice == "3":
        t_id = int(input("Enter ID of the district to update: "))
        new_name = input("Enter new name: ")
        update(t_id, new_name)
    elif choice == "4":
        t_id = int(input("Enter ID of the district to delete: "))
        delete(t_id)
    elif choice == "5":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
