# Pet Disease Diagnosis Expert System

## Overview

The **Pet Disease Diagnosis Expert System** is a rule-based expert system designed to assist in diagnosing common diseases in cats and dogs. Developed using the Python-based **Experta** framework, this system utilizes a forward-chaining inference mechanism to derive diagnoses based on user-provided symptoms, animal details, and duration of the illness.

This project demonstrates the potential of expert systems in veterinary diagnostics by providing accurate disease predictions and detailed reasoning for diagnoses.

---

## Features

- **Rule-Based Reasoning**: Implements forward-chaining logic to evaluate user-provided facts against a predefined set of rules.
- **Comprehensive Disease Rules**: Includes rules for common diseases in cats and dogs such as Parvovirus, Canine Distemper, Upper Respiratory Infection, and Feline Calicivirus.
- **Confidence-Based Diagnosis**: Offers possible diagnoses with confidence levels when there is no exact rule match for the given inputs.
- **Diagnostic Explanation**: Provides detailed reasoning for diagnoses, explaining how each conclusion is derived based on matching facts.
- **User-Friendly Interface**: Simplified interaction to input symptoms and receive diagnoses.

---

## How It Works

1. **Input Facts**: Users provide details such as the animal type (Cat or Dog), symptoms (e.g., lethargy, fever, diarrhea), duration of illness, and age of the animal.
2. **Rule Evaluation**: The system evaluates user-provided facts against predefined disease rules using forward chaining.
3. **Diagnosis**:
   - If a rule is matched, the system provides a definitive diagnosis.
   - If no exact rule matches, the system calculates confidence levels for possible diagnoses based on partially matching rules.
4. **Explanation**: The system generates a reasoning summary, detailing how the diagnosis or possible diagnoses were determined.

---

## Technologies Used

- **Experta Framework**: A Python-based library for building rule-based expert systems.
- **Streamlit**: Used for creating a user-friendly web-based interface for interacting with the expert system.
- **Python**: Core programming language for the implementation.

---

## Applications

This project can serve as a foundational tool for:
- Veterinary diagnostics for pets.
- Educational purposes to demonstrate the working of rule-based expert systems.
- Extending to other domains such as human healthcare.

---

## Future Enhancements

- **Expand Disease Database**: Add more rules for a broader range of diseases in cats and dogs.
- **Integration with Machine Learning**: Enhance the system with hybrid approaches that combine rule-based reasoning and data-driven insights.
- **Enhanced User Interface**: Improve the user experience with advanced UI/UX design.

---
