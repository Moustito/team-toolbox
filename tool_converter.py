"""
Tool 1 – Temperature converter 🌡️

Write two functions: celsius_to_fahrenheit(c) and fahrenheit_to_celsius(f). They return the result rounded to 1 decimal.
run() asks the direction of the conversion, then the temperature, and displays the result.
Formulas: F = C × 9/5 + 32 and C = (F − 32) × 5/9

Convert (1) Celsius → Fahrenheit or (2) Fahrenheit → Celsius? 1
Temperature: 25
25.0 °C = 77.0 °F

⭐ Bonus: if the user types something other than 1 or 2, display an error message.
"""

def celsius_to_fahrenheit(c):
    """convert Celsius to Fahrenheit."""
    return round(c * 9 / 5 + 32, 1)

def fahrenheit_to_celsius(f):
    """convert Fahrenheit to Celsius."""
    return round((f - 32) * 5 / 9, 1)

if __name__ == "__main__":
    run()