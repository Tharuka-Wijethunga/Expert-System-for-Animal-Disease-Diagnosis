import streamlit as st
from experta import Fact
from rules import AnimalDiagnosisExpert
from knowledge import animal_symptoms, animal_types, validate_input

# Streamlit UI setup
st.title("🐶 Animal Disease Diagnosis Expert System")


# Initialize session state with default values
def init_session_state():
    defaults = {
        "facts": {},
        "engine": AnimalDiagnosisExpert(),
        "current_step": "ask_animal_type",
        "animal_type": "",
        "symptoms": [],
        "duration": "",
        "age": ""
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# Initialize session state
init_session_state()


# Reset function
def reset_session():
    for key in ["facts", "engine", "current_step", "animal_type", "symptoms", "duration", "age"]:
        del st.session_state[key]
    init_session_state()


# Step-by-step questionnaire
def animal_type_step():
    st.header("Animal Type")
    animal_type = st.text_input("What type of animal? (Dog or Cat)",
                                value=st.session_state.get("animal_type", "")).title()

    if st.button("Next"):
        if animal_type in animal_types:
            st.session_state.animal_type = animal_type
            st.session_state.facts["animal_type"] = animal_type
            st.session_state.current_step = "ask_symptoms"
            st.rerun()
        else:
            st.warning("Please enter a valid animal type (Dog or Cat).")


def symptoms_step():
    st.header("Symptoms")
    symptoms_input = st.text_input("What symptoms does the animal show? (Comma-separated)",
                                   value=", ".join(st.session_state.get("symptoms", [])))

    if st.button("Next"):
        user_symptoms = [s.strip().lower() for s in symptoms_input.split(",") if s.strip() in animal_symptoms]

        if user_symptoms:
            st.session_state.symptoms = user_symptoms
            for symptom in user_symptoms:
                st.session_state.facts[f"symptom_{symptom}"] = True
            st.session_state.current_step = "ask_duration"
            st.rerun()
        else:
            st.warning("Please enter valid symptoms.")


def duration_step():
    st.header("Symptom Duration")
    duration = st.text_input("How long has the animal been showing symptoms?",
                             value=st.session_state.get("duration", ""))

    if st.button("Next"):
        if duration:
            st.session_state.duration = duration
            st.session_state.facts["duration"] = duration
            st.session_state.current_step = "ask_age"
            st.rerun()
        else:
            st.warning("Please enter the symptom duration.")


def age_step():
    st.header("Animal Age")
    age = st.text_input("What is the animal's age?",
                        value=st.session_state.get("age", ""))

    if st.button("Next"):
        if age:
            st.session_state.age = age
            st.session_state.facts["age"] = age
            st.session_state.current_step = "diagnose"
            st.rerun()
        else:
            st.warning("Please enter the animal's age.")


def diagnose_step():
    st.header("Diagnosis")
    engine = st.session_state.engine
    engine.reset()

    for fact_name, fact_value in st.session_state.facts.items():
        engine.declare(Fact(**{fact_name: fact_value}))

    engine.run()

    if hasattr(engine, "result"):
        st.success(engine.result)
    else:
        st.error("No diagnosis found for the given symptoms.")

    if st.button("Diagnose Another Animal"):
        reset_session()


# Main application flow
def main():
    # Add a sidebar for navigation or reset
    st.sidebar.title("Navigation")
    if st.sidebar.button("Reset Diagnosis"):
        reset_session()

    # Render the appropriate step based on current_step
    if st.session_state.current_step == "ask_animal_type":
        animal_type_step()
    elif st.session_state.current_step == "ask_symptoms":
        symptoms_step()
    elif st.session_state.current_step == "ask_duration":
        duration_step()
    elif st.session_state.current_step == "ask_age":
        age_step()
    elif st.session_state.current_step == "diagnose":
        diagnose_step()


# Run the main application
if __name__ == "__main__":
    main()