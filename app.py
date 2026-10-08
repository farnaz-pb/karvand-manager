import json

with open("data/karvands.json", "r") as file:
    karvands_manager = json.load(file)
while True:
    print("-------------------------------")
    print("*Menu*")
    print("1-Add\n2-Show all")
    print("3-Search by id\n4-Search by skills")
    print("5-Edit\n6-Delete")
    print("7-Report\n8-Exit")
    user_choice = int(input("Select an option : "))
    if user_choice == 1:
        name = input("Full_Name : ")
        # checking that karvand is exist already or not
        for karvand in karvands_manager["karvands"].values():
            if karvand["full_name"] == name:
                exists = True
                break
        if exists:
            print("This karvand already exists.")
            continue
        # if we had no user
        if len(karvands_manager["karvands"]) == 0:
            id = 1
        else:
            id = 0
            # loop for save the last Id
            for karvand in karvands_manager["karvands"].values():
                if karvand["id"] > id:
                    id = karvand["id"]
            id += 1
        email = input("Email : ")
        city = input("City : ")
        education_d = input("Education Degree : ")
        education_f = input("Education Field : ")
        education = {"degree": education_d, "field": education_f}
        skills = []
        while True:
            skill_n = input("Skill Name : ")
            skill_l = input("Skill Level : ")
            while True:
                try:
                    skill_s = int(input("Skill Score : "))
                    if skill_s < 0 or skill_s > 100:
                        print("Incorrect number! It should be between 0-100.")
                    else:
                        break
                except ValueError:
                    print("Invalid value! Enter a number please.")
            skill = {"name": skill_n, "level": skill_l, "score": skill_s}
            skills.append(skill)
            another_skill = input("Add another skill? (yes or no) : ")
            if another_skill != "yes":
                break
            karvands = {
                "id": id,
                "full_name": name,
                "email": email,
                "city": city,
                "education": education,
                "skills": skills,
            }
            karvands_manager["karvands"][id] = karvands
            with open("data/karvands.json", "w") as file:
                json.dump(karvands_manager, file, indent=4)
                # dump : save the python data in JSON format and write it to file
                # indent=4 : stores the information more neatly in the JSON file
            print("Karvand added successfully!")

    elif user_choice == 2:
        with open("data/karvands.json", "r") as file:
            karvands_manager = json.load(file)
        if len(karvands_manager["karvands"]) == 0:
            print("No karvand have been added yet!")
        else:
            for karvand in karvands_manager["karvands"].values():
                print("-------------------------------")
                print("Id : ", karvand["id"])
                print("Full Name : ", karvand["full_name"])
                print("Email : ", karvand["email"])
                print("City : ", karvand["city"])
                print("Education : ", karvand["education"]["degree"])
                print("Education : ", karvand["education"]["field"])
                print("Skills")
                for skill in karvand["skills"]:
                    print("Name :", skill["name"])

    elif user_choice == 3:
        with open("data/karvands.json", "r") as file:
            karvands_manager = json.load(file)
        try:
            search_id = int(input("Enter ID : "))
        except ValueError:
            print("Invalid ID! Enter a number.")
            continue
        found = False
        for karvand in karvands_manager["karvands"].values():
            if karvand["id"] == search_id:
                print("-------------------------------")
                print("ID :", karvand["id"])
                print("Full Name :", karvand["full_name"])
                print("Email :", karvand["email"])
                print("City :", karvand["city"])
                print("Education Degree :", karvand["education"]["degree"])
                print("Education Field :", karvand["education"]["field"])
                print("Skills :")
                for skill in karvand["skills"]:
                    print("Name :", skill["name"])
                    print("Level :", skill["level"])
                    print("Score :", skill["score"])
                found = True
                break
        if found == False:
            print("No karvand found with this ID.")

    elif user_choice == 4:
        with open("data/karvands.json", "r") as file:
            karvands_manager = json.load(file)
        search_skill = input("ُSkill Name : ")
        found = False
        for karvand in karvands_manager["karvands"].values():
            for skill in karvand["skills"]:
                if skill["name"] == search_skill:
                    print("ID :", karvand["id"])
                    print("Full Name :", karvand["full_name"])
                    print("Email :", karvand["email"])
                    print("City :", karvand["city"])
                    print("Skill :", skill["name"])
                    print("Level :", skill["level"])
                    print("Score :", skill["score"])
                    found = True
        if found == False:
            print("No karvand found with this skill.")

    elif user_choice == 5:
        with open("data/karvands.json", "r") as file:
            karvands_manager = json.load(file)
        try:
            edit_id = int(input("Enter ID : "))
        except ValueError:
            print("Invalid ID! Enter a number.")
            continue
        found = False
        for karvand in karvands_manager["karvands"].values():
            if karvand["id"] == edit_id:
                found = True
                print("1-Email")
                print("2-City")
                print("3-Education Degree")
                print("4-Education Field")
                try:
                    edit_choice = int(input("Select what you want to edit : "))
                except ValueError:
                    print("Invalid input! Enter a number.")
                    break
                if edit_choice == 1:
                    karvand["email"] = input("New Email : ")
                elif edit_choice == 2:
                    karvand["city"] = input("New City : ")
                elif edit_choice == 3:
                    karvand["education"]["degree"] = input("New Education Degree : ")
                elif edit_choice == 4:
                    karvand["education"]["field"] = input("New Education Field : ")
                else:
                    print("Invalid option!")
                    break
                with open("data/karvands.json", "w") as file:
                    json.dump(karvands_manager, file, indent=4)
                print("Karvand updated successfully!")
                break
        if found == False:
            print("No karvand found with this ID.")

    elif user_choice == 6:
        with open("data/karvands.json", "r") as file:
            karvands_manager = json.load(file)
        try:
            delete_id = int(input("Enter ID : "))
        except ValueError:
            print("Invalid ID! Enter a number.")
            continue
        found = False
        for key, karvand in karvands_manager["karvands"].items():
            if karvand["id"] == delete_id:
                del karvands_manager["karvands"][key]
                with open("data/karvands.json", "w") as file:
                    json.dump(karvands_manager, file, indent=4)
                print("Karvand deleted successfully!")
                found = True
                break
        if found == False:
            print("No karvand found with this ID.")

    elif user_choice == 7:
        with open("data/karvands.json", "r") as file:
            karvands_manager = json.load(file)
        total_karvands = len(karvands_manager["karvands"])
        total_skills = 0
        total_score = 0
        cities = []
        unique_skills = []
        for karvand in karvands_manager["karvands"].values():
            if karvand["city"] not in cities:
                cities.append(karvand["city"])
            for skill in karvand["skills"]:
                total_skills += 1
                total_score += skill["score"]
                if skill["name"] not in unique_skills:
                    unique_skills.append(skill["name"])
        if total_skills == 0:
            average_score = 0
        else:
            average_score = total_score / total_skills
        report = {
            "total_karvands": total_karvands,
            "total_skills": total_skills,
            "average_skill_score": average_score,
            "cities": cities,
            "unique_skills": unique_skills,
        }
        print("Total Karvands :", total_karvands)
        print("Total Skills :", total_skills)
        print("Average Skill Score :", average_score)
        print("Cities :", cities)
        print("Unique Skills :", unique_skills)
        with open("data/report.json", "w") as file:
            json.dump(report, file, indent=4)
        print("Report saved successfully!")

    elif user_choice == 8:
        print("GoodBye!")
        break
