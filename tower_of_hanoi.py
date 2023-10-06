def tower_of_hanoi(n, source_peg, auxiliary_peg, target_peg):
    if n == 1:
        print(f"Move disk 1 from {source_peg} to {target_peg}")
        return
    tower_of_hanoi(n - 1, source_peg, target_peg, auxiliary_peg)
    print(f"Move disk {n} from {source_peg} to {target_peg}")
    tower_of_hanoi(n - 1, auxiliary_peg, source_peg, target_peg)

# Input from the user
n = int(input("Enter the number of disks: "))
source_peg = input("Enter the name of the source peg (e.g., 'A'): ").strip().upper()
auxiliary_peg = input("Enter the name of the auxiliary peg (e.g., 'B'): ").strip().upper()
target_peg = input("Enter the name of the target peg (e.g., 'C'): ").strip().upper()

# Ensure peg names are distinct
while source_peg == auxiliary_peg or source_peg == target_peg or auxiliary_peg == target_peg:
    print("Peg names must be distinct. Please enter again.")
    source_peg = input("Enter the name of the source peg: ").strip().upper()
    auxiliary_peg = input("Enter the name of the auxiliary peg: ").strip().upper()
    target_peg = input("Enter the name of the target peg: ").strip().upper()

# Call the tower_of_hanoi function with user input
tower_of_hanoi(n, source_peg, auxiliary_peg, target_peg)
