def tower_of_hanoi(n, source, helper, target):
    if n == 1:
        print(f"Move disk {n} from {source} to {target}")
        return

    tower_of_hanoi(n - 1, source, target, helper)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, helper, source, target)


# Example usage
if __name__ == "__main__":
    n = 4  # Number of disks
    tower_of_hanoi(n, 'S', 'H', 'D')  # S is source, D is target, H is helper
