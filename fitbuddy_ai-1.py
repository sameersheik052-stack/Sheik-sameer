import os
import sys
from google import genai
from google.genai import types


def generate_fitness_plan():
    # 1. Initialize the Gemini Client
    # The client automatically picks up the GEMINI_API_KEY environment variable.
    try:
        client = genai.Client()
    except Exception as e:
        print(f"Error initializing Gemini Client: {e}")
        print("Please ensure your GEMINI_API_KEY environment variable is set properly.")
        sys.exit(1)

    print("=== Welcome to FitBuddy-AI: Your Personal Fitness & Diet Planner ===")
    print("Please provide some basic details to tailor your routine:\n")

    # 2. Collect user parameters
    try:
        age = input("Enter your age: ").strip()
        gender = input("Enter your gender: ").strip()
        weight = input("Enter your weight (e.g., 70 kg or 150 lbs): ").strip()
        height = input("Enter your height (e.g., 175 cm or 5'9\"): ").strip()
        goal = input(
            "Enter your primary goal (e.g., Weight Loss, Muscle Gain, Endurance): "
        ).strip()
        activity_level = input(
            "Current activity level (e.g., Sedentary, Lightly Active, Very Active): "
        ).strip()
        dietary_pref = input(
            "Dietary preference (e.g., Vegan, Keto, Omnivore, No restrictions): "
        ).strip()
        days_per_week = input(
            "How many days per week can you workout? "
        ).strip()
    except KeyboardInterrupt:
        print("\nExiting FitBuddy-AI. Stay active!")
        sys.exit(0)

    # 3. Construct a clear prompt for the Gemini model
    prompt = f"""
You are an expert personal trainer and certified sports nutritionist.
Create a comprehensive, highly customized 7-day fitness and meal plan
based on the following user profile:

- Age: {age}
- Gender: {gender}
- Weight: {weight}
- Height: {height}
- Primary Goal: {goal}
- Activity Level: {activity_level}
- Dietary Preference: {dietary_pref}
- Workout Availability: {days_per_week} days per week

Please format the response clearly with markdown headings, covering:
1. **Overview & Caloric Strategy**: Estimated daily caloric target and macro breakdown.
2. **Workout Routine**: Structured schedule matching their availability,
   including warm-ups, main exercises (sets/reps), and cool-downs.
3. **Meal Plan Suggestions**: Daily template or sample meal ideas
   (Breakfast, Lunch, Dinner, Snacks) matching their dietary preferences.
4. **Pro-Tips**: Crucial advice regarding hydration, sleep, and recovery.

Include a brief note that calorie and exercise recommendations are estimates
and users with medical conditions should consult an appropriate professional.
"""

    print(
        "\n[FitBuddy-AI is analyzing your profile and designing your custom "
        "blueprint... Please wait]\n"
    )

    try:
        # 4. Generate content using the Gemini model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=1500,
            ),
        )

        # 5. Output the results
        print("=" * 60)
        print("YOUR CUSTOM FITBUDDY-AI PLAN")
        print("=" * 60)
        print(response.text)
        print("=" * 60)

    except Exception as e:
        print(f"An error occurred while generating the plan: {e}")


if __name__ == "__main__":
    generate_fitness_plan()
