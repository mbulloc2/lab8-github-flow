from rich.console import Console
from rich.prompt import Prompt
from adventure.utils import read_events_from_file
import random

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[cyan]You wake up in a dark forest. You can go left or right.[/cyan]")
    while True:
        choice = Prompt.ask(
        "Which direction do you choose? (left/right/exit)",
        choices=["left", "right", "exit"]
        )

        if choice == 'exit':
            break
        
        console.print(step(choice, events))

