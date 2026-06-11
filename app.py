from flask import Flask, render_template, request

app = Flask(__name__)

# --- Emission Factors ---
FACTORS = {
    "transport": 0.3,
    "electricity": 0.5,
    "food": 0.2
}

# --- Validation Function ---
def validate_input(value, field_name: str) -> float:
    """
    Validate that input is a non-negative number.
    Args:
        value (str): Input from form
        field_name (str): Name of the field (for error messages)
    Returns:
        float: Validated numeric value
    """
    try:
        num = float(value)
        if num < 0:
            raise ValueError(f"{field_name} must be non-negative")
        return num
    except ValueError:
        raise ValueError(f"{field_name} must be a valid number")

# --- Emission Calculation ---
def calculate_emissions(transport: float, electricity: float, food: float) -> float:
    """
    Optimized emission calculation.
    Args:
        transport (float): Transport usage value
        electricity (float): Electricity usage value
        food (float): Food consumption value
    Returns:
        float: Carbon footprint in kg CO₂/day
    """
    factors = FACTORS
    return (transport * factors["transport"] +
            electricity * factors["electricity"] +
            food * factors["food"])


# --- AI Suggestions ---
def suggest_actions(footprint: float) -> str:
    """
    Suggest eco-friendly actions based on footprint.
    Args:
        footprint (float): Carbon footprint in kg CO₂/day
    Returns:
        str: Suggestion message
    """
    if footprint > 10:
        return "Try reducing electricity usage or carpooling."
    elif footprint > 5:
        return "Consider walking, cycling, or eating less meat."
    else:
        return "Great job! Keep tracking your footprint."

# --- Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        transport = validate_input(request.form.get('transport', 0), "Transport")
        electricity = validate_input(request.form.get('electricity', 0), "Electricity")
        food = validate_input(request.form.get('food', 0), "Food")

        footprint = calculate_emissions(
            transport=transport,
            electricity=electricity,
            food=food
        )
        suggestion = suggest_actions(footprint)

        return f"Your estimated carbon footprint is {footprint:.2f} kg CO₂/day.<br>{suggestion}"
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception:
        return "An unexpected error occurred. Please check your inputs."

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
