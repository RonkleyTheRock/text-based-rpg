print()
print("Select your class")
print()
print("1. Occultist")
print("2. Alchemist")
print("3. Arcanist")
print("4. Vanguard")
print("5. Duelist")
print("6. Trickster")
print("7. Priest")

class_choice = input("Choose a class: ")

if class_choice == "1":
    selected_class = "Occultist"

elif class_choice == "2":
    selected_class = "Alchemist"

elif class_choice == "3":
    selected_class = "Arcanist"

elif class_choice == "4":
    selected_class = "Vanguard"

elif class_choice == "5":
    selected_class = "Duelist"

elif class_choice == "6":
    selected_class = "Trickster"

elif class_choice == "7":
    selected_class = "Priest"

else:
    print("Invalid option.")

print("You selected:", selected_class)
