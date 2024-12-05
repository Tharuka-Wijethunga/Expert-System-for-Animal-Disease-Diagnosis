from experta import Fact, KnowledgeEngine, Rule

# Predefined symptoms, animal types, ages, and durations for the expert system
animal_symptoms = [
    "fever", "lethargy", "coughing", "diarrhea", "skin_lesions",
    "appetite_loss", "vomiting", "nasal_discharge"
]

animal_types = ["Dog", "Cat"]
ages = ["< 5 yrs", "5 - 10 yrs", "10 < yrs"]
durations = ["less than 5 days", "5 - 10 days", "more than 10 days"]

# Utility function to validate user input
def validate_input(user_input, valid_options):
    """
    Validates user input against a list of valid options.
    Returns the matching option or None if no match found.
    """
    user_input_lower = user_input.strip().lower()
    for option in valid_options:
        if user_input_lower == option.lower():
            return option
    return None