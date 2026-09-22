#project_3: Collection Manipulator

print("Welcome to the Student Data Management System!")
    
student_records = []
    
all_subjects_set = set()
    
while True:
    print("\n--- Menu Options ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information (Age or Subjects)")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
        
    choice = input("\nEnter your choice (1-6): ").strip()
        
    if choice == '1':
        print("\nAdd New Student")
        name = input("Enter student name: ").strip()
        age = int(input("Enter age: ").strip())
        grade = input("Enter grade: ").strip()
            
        subjects_input = input("Enter subjects (comma-separated): ").strip()
        subjects_set = {sub.strip() for sub in subjects_input.split(',') if sub.strip()}
            
        student_id = input("Enter student ID: ").strip()
        dob = input("Enter date of birth (DD-MM-YYYY): ").strip()
            
        id_dob_tuple = (student_id, dob)
   
        all_subjects_set.update(subjects_set)
            
        student_dict = {'id_dob': id_dob_tuple,'name': name,'age': age,'grade': grade,'subjects': subjects_set}
        
        student_records.append(student_dict)
        print(f"\nStudent added successfully")
            
    elif choice == '2':
        if not student_records:
            print("\n[Notice] No student records available.")
        else:
            print("\n ALL STUDENTS ")
            for student in student_records:
                s_id, s_dob = student['id_dob']
                subjects_formatted = ", ".join(student['subjects'])
                print(f"ID: {s_id}")
                print(f"DOB: {s_dob}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Grade: {student['grade']}")
                print(f"Subjects: {subjects_formatted}")
                
                    
    elif choice == '3':
        target_id = input("\nEnter the Student ID to update: ").strip()
        found = False
            
        for student in student_records:
             
            if student['id_dob'][0] == target_id:
                found = True
                print(f"\nFound student: {student['name']}")
                print("What would you like to update?")
                print("1. Age")
                print("2. Subjects")
                up_choice = input("Enter choice (1 or 2): ").strip()
                    
                if up_choice == '1':
                    student['age'] = int(input("Enter new age: ").strip())
                    print("Age updated successfully!")
                elif up_choice == '2':
                    new_sub_input = input("Enter new subjects (comma-separated): ").strip()
                    new_subjects_set = {sub.strip() for sub in new_sub_input.split(',') if sub.strip()}
                    student['subjects'] = new_subjects_set
                    all_subjects_set.update(new_subjects_set)
                    print("Subjects updated successfully!")
                else:
                    print("Invalid update choice.")
                break
                    
        if not found:
            print("\nStudent ID not found.")
                
    elif choice == '4':
        target_id = input("\nEnter the Student ID to delete: ").strip()
        deleted = False
            
        for index, student in enumerate(student_records):
            if student['id_dob'][0] == target_id:
                    
                del student_records[index]
                deleted = True
                print("\nStudent record deleted successfully!")
                break
                    
        if not deleted:
            print("\n Student ID not found.")
                
    elif choice == '5':
        if not all_subjects_set:
            print("\n[Notice] No subjects recorded yet.")
        else:
            print("\nUnique Subjects Offered (No Duplicates) ")
            for sub in all_subjects_set:
                print(f"- {sub}")
                    
    elif choice == '6':
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")
