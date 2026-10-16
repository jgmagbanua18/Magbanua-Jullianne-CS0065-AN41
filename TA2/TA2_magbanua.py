import random

# Environment
rooms = {
    "A": input("Enter Room A state (Dirty/Clean): ").capitalize(),
    "B": input("Enter Room B state (Dirty/Clean): ").capitalize(),
    "C": input("Enter Room C state (Dirty/Clean): ").capitalize()
}


def is_dirty(room):
    """Check if a room is dirty."""
    return rooms[room] == "Dirty"


def clean_room(room):
    """Clean the specified room."""
    rooms[room] = "Clean"


# Bonus 4: Text-Based Visualization
def display_grid(agent):
    print("\nROOM MAP")

    for room in ["A", "B", "C"]:
        if room == agent.location:
            print(f"[{room}: {rooms[room]} 🤖]", end=" ")
        else:
            print(f"[{room}: {rooms[room]}]", end=" ")

    print("\n")


# Rule-Based Agent
class VacuumAgent:
    def __init__(self):
        self.location = "A"

    # Three-room movement
    def move(self):
        if self.location == "A":
            self.location = "B"
        elif self.location == "B":
            self.location = "C"
        else:
            self.location = "A"

    # Randomly choose a dirty room
    def perceive_and_act(self):

        # Rule 1: Clean current room if dirty
        if is_dirty(self.location):
            clean_room(self.location)
            return f"Cleaned Room {self.location}"

        # Find all dirty rooms
        dirty_rooms = []

        for room in rooms:
            if rooms[room] == "Dirty":
                dirty_rooms.append(room)

        # Move to a random dirty room if any exist
        if dirty_rooms:
            self.location = random.choice(dirty_rooms)
            return f"Moved to dirty Room {self.location}"

        # Otherwise continue normal movement
        self.move()
        return f"Moved to Room {self.location}"


# Create the agent
agent = VacuumAgent()

# Run the Simulation
steps = int(input("Enter number of steps: "))

print("\nVACUUM CLEANER SIMULATION")
print("=" * 35)

for step in range(1, steps + 1):

    print(f"\nStep {step}")
    print("-" * 20)
    print(f"Current Location: {agent.location}")

    action = agent.perceive_and_act()

    print(f"Action Taken: {action}")
    print("Environment State:")
    print(rooms)

    # Visualize agent position
    display_grid(agent)