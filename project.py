import random
from IPython.display import display, clear_output
import ipywidgets as widgets

# --- Game Setup ---
# Select a random number between 1 and 50
TARGET_NUMBER = random.randint(1, 50)
MAX_CHANCES = 5
current_score = MAX_CHANCES

# --- Widget Definitions ---

# 1. Output area for dynamic text (hints, messages)
output = widgets.Output()

# 2. Text input for the user's guess
guess_input = widgets.IntText(
    value=1,
    description='Your Guess (1-50):',
    disabled=False,
    min=1,
    max=50,
    style={'description_width': 'initial'}
)

# 3. Label to display the current score
score_label = widgets.Label(f"Score out of {MAX_CHANCES}: {current_score}")

# 4. Button to trigger the check function
check_button = widgets.Button(
    description='CHECK',
    disabled=False,
    button_style='primary',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click to check your guess'
)

# --- Game Logic Function ---

def check_guess(b):
    """Handles the logic when the CHECK button is clicked."""
    global current_score
    user_guess = guess_input.value

    # Use 'output' context to clear previous messages and print new ones
    with output:
        clear_output(wait=True)

        # Check if the game is over
        if current_score <= 0:
            print("❌ Game Over! You lost all your chances.")
            print(f"The number was {TARGET_NUMBER}.")
            check_button.disabled = True
            return

        # Handle invalid guess range (as per your original code logic)
        if user_guess > 50 or user_guess < 1:
            print("⚠️ Invalid input! Please guess a number between 1 and 50.")
            # Your original code penalizes for this, so we'll do the same:
            current_score -= 1
            print("You just lost 1 chance.")

        # Handle correct guess
        elif user_guess == TARGET_NUMBER:
            print(f"🎉 CONGRATULATIONS! You won! The number was {TARGET_NUMBER}.")
            print(f"Final Score: {current_score}")
            check_button.disabled = True # Disable the button once won
            guess_input.disabled = True

        # Handle guess too low
        elif user_guess < TARGET_NUMBER:
            current_score -= 1
            print("⬇️ Your guess was too low: Guess a number higher.")

        # Handle guess too high
        elif user_guess > TARGET_NUMBER:
            current_score -= 1
            print("⬆️ Your guess was too High: Guess a number lower.")

        # After the check, update the score label
        score_label.value = f"Score out of {MAX_CHANCES}: {current_score}"

        # Final check for game over after a move
        if current_score <= 0 and user_guess != TARGET_NUMBER:
            clear_output(wait=True)
            print("❌ Game Over! You lost all your chances.")
            print(f"The number was {TARGET_NUMBER}.")
            check_button.disabled = True
            guess_input.disabled = True


# --- Wiring the Button to the Function ---
check_button.on_click(check_guess)

# --- Layout and Display ---

# Create a container for the title/instructions
title = widgets.Label('I challenge you to guess the number (1-50)', style={'font_weight': 'bold'})

# Arrange the widgets vertically
game_ui = widgets.VBox([
    title,
    guess_input,
    check_button,
    score_label,
    widgets.HBox([widgets.Label("Hint:"), output])
])

# Display the entire UI
display(game_ui)
