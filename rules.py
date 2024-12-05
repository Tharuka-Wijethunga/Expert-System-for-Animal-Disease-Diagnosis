from experta import *

class AnimalDiagnosisExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.matched_rules = []
        self.result = None

    # Dog Disease Rules
    @Rule(
        Fact(animal_type="Dog"),
        Fact(symptom_lethargy=True),
        Fact(symptom_fever=True),
        Fact(symptom_diarrhea=True),
        Fact(duration__in=["less than 5 days", "5 - 10 days"]),
        Fact(age="< 5 yrs")
    )
    def rule_parvovirus(self):
        self.declare(Fact(disease="Parvovirus"))

    @Rule(
        Fact(animal_type="Dog"),
        Fact(symptom_lethargy=True),
        Fact(symptom_fever=True),
        Fact(symptom_vomiting=True),
        Fact(symptom_coughing=True),
        Fact(duration__in=["less than 5 days", "5 - 10 days"]),
        Fact(age="< 5 yrs")
    )
    def rule_canine_distemper(self):
        self.declare(Fact(disease="Canine Distemper"))

    @Rule(
        Fact(animal_type="Dog"),
        Fact(symptom_lethargy=True),
        Fact(symptom_fever=True),
        Fact(symptom_vomiting=True),
        Fact(symptom_diarrhea=True),
        Fact(duration="less than 5 days"),
        Fact(age__in=["5 - 10 yrs", "< 5 yrs"])
    )
    def rule_heat_stroke(self):
        self.declare(Fact(disease="Heat Stroke"))

    # Cat Disease Rules
    @Rule(
        Fact(animal_type="Cat"),
        Fact(symptom_fever=True),
        Fact(symptom_coughing=True),
        Fact(symptom_skin_lesions=True),
        Fact(duration="5 - 10 days"),
        Fact(age="< 5 yrs")
    )
    def rule_upper_respiratory_infection(self):
        self.declare(Fact(disease="Upper Respiratory Infection"))

    @Rule(
        Fact(animal_type="Cat"),
        Fact(symptom_coughing=True),
        Fact(symptom_fever=True),
        Fact(symptom_appetite_loss=True),
        Fact(duration="5 - 10 days"),
        Fact(age="< 5 yrs")
    )
    def rule_feline_calicivirus(self):
        self.declare(Fact(disease="Feline Calicivirus"))

    # General Rules
    @Rule(
        Fact(symptom_lethargy=True),
        Fact(symptom_appetite_loss=True),
        Fact(duration="more than 10 days"),
        Fact(age="10 < yrs")
    )
    def rule_anemia(self):
        self.declare(Fact(disease="Anemia"))

    @Rule(
        Fact(symptom_vomiting=True),
        Fact(symptom_diarrhea=True),
        Fact(duration="less than 5 days"),
        Fact(age="< 5 yrs")
    )
    def rule_food_poisoning(self):
        self.declare(Fact(disease="Food Poisoning"))

    @Rule(Fact(disease=MATCH.disease))
    def conclude_diagnosis(self, disease):
        # Collect all the facts that contributed to the diagnosis
        matched_facts = []
        for fact in self.facts.values():
            if isinstance(fact, Fact) and fact != Fact(disease=disease):  # Exclude the disease fact
                fact_str = ", ".join([f"{key}: {value}" for key, value in fact.items() if key != "__factid__"])
                matched_facts.append(fact_str)

        # Build the diagnostic explanation
        matched_facts_str = "\n".join([f"- {fact}" for fact in matched_facts])
        reasoning = f"""Diagnosis: {disease}

        Diagnostic Explanation:
        This diagnosis is based on the following facts:
        {matched_facts_str} 
        """
        self.result = reasoning

    rule_fact_mapping = [
        {
            "disease": "Parvovirus",
            "facts": {
                "animal_type": "Dog",
                "symptom_lethargy": True,
                "symptom_fever": True,
                "symptom_diarrhea": True,
                "duration": ["less than 5 days", "5 - 10 days"],
                "age": "< 5 yrs",
            },
        },
        {
            "disease": "Canine Distemper",
            "facts": {
                "animal_type": "Dog",
                "symptom_lethargy": True,
                "symptom_fever": True,
                "symptom_vomiting": True,
                "symptom_coughing": True,
                "duration": ["less than 5 days", "5 - 10 days"],
                "age": "< 5 yrs",
            },
        },
        {
            "disease": "Heat Stroke",
            "facts": {
                "animal_type": "Dog",
                "symptom_lethargy": True,
                "symptom_fever": True,
                "symptom_vomiting": True,
                "symptom_diarrhea": True,
                "duration": "less than 5 days",
                "age": ["5 - 10 yrs", "< 5 yrs"],
            },
        },
        {
            "disease": "Upper Respiratory Infection",
            "facts": {
                "animal_type": "Cat",
                "symptom_fever": True,
                "symptom_coughing": True,
                "symptom_skin_lesions": True,
                "duration": "5 - 10 days",
                "age": "< 5 yrs",
            },
        },
        {
            "disease": "Feline Calicivirus",
            "facts": {
                "animal_type": "Cat",
                "symptom_coughing": True,
                "symptom_fever": True,
                "symptom_appetite_loss": True,
                "duration": "5 - 10 days",
                "age": "< 5 yrs",
            },
        },
        {
            "disease": "Anemia",
            "facts": {
                "symptom_lethargy": True,
                "symptom_appetite_loss": True,
                "duration": "more than 10 days",
                "age": "10 < yrs",
            },
        },
        {
            "disease": "Food Poisoning",
            "facts": {
                "symptom_vomiting": True,
                "symptom_diarrhea": True,
                "duration": "less than 5 days",
                "age": "< 5 yrs",
            },
        },
    ]

    @Rule(NOT(Fact(disease=MATCH.disease)))  # Triggered when no disease has been declared
    def conclude_possible_diagnoses(self):
        # Debugging: Ensure the function is triggered
        print("Triggered `conclude_possible_diagnoses`")

        # Map rules to their facts
        rule_fact_mapping = [
            {
                "disease": "Parvovirus",
                "facts": {
                    "animal_type": "Dog",
                    "symptom_lethargy": True,
                    "symptom_fever": True,
                    "symptom_diarrhea": True,
                    "duration": ["less than 5 days", "5 - 10 days"],
                    "age": "< 5 yrs",
                },
            },
            {
                "disease": "Canine Distemper",
                "facts": {
                    "animal_type": "Dog",
                    "symptom_lethargy": True,
                    "symptom_fever": True,
                    "symptom_vomiting": True,
                    "symptom_coughing": True,
                    "duration": ["less than 5 days", "5 - 10 days"],
                    "age": "< 5 yrs",
                },
            },
            {
                "disease": "Heat Stroke",
                "facts": {
                    "animal_type": "Dog",
                    "symptom_lethargy": True,
                    "symptom_fever": True,
                    "symptom_vomiting": True,
                    "symptom_diarrhea": True,
                    "duration": "less than 5 days",
                    "age": ["5 - 10 yrs", "< 5 yrs"],
                },
            },
            {
                "disease": "Upper Respiratory Infection",
                "facts": {
                    "animal_type": "Cat",
                    "symptom_fever": True,
                    "symptom_coughing": True,
                    "symptom_skin_lesions": True,
                    "duration": "5 - 10 days",
                    "age": "< 5 yrs",
                },
            },
            {
                "disease": "Feline Calicivirus",
                "facts": {
                    "animal_type": "Cat",
                    "symptom_coughing": True,
                    "symptom_fever": True,
                    "symptom_appetite_loss": True,
                    "duration": "5 - 10 days",
                    "age": "< 5 yrs",
                },
            },
            {
                "disease": "Anemia",
                "facts": {
                    "symptom_lethargy": True,
                    "symptom_appetite_loss": True,
                    "duration": "more than 10 days",
                    "age": "10 < yrs",
                },
            },
            {
                "disease": "Food Poisoning",
                "facts": {
                    "symptom_vomiting": True,
                    "symptom_diarrhea": True,
                    "duration": "less than 5 days",
                    "age": "< 5 yrs",
                },
            },
        ]

        # Collect all input facts
        input_facts = {}
        for fact in self.facts.values():
            if isinstance(fact, Fact):
                input_facts.update({key: value for key, value in fact.items() if key != "__factid__"})

        # Debugging: Print input facts
        print("Input facts:", input_facts)

        # Calculate confidence levels and reasoning
        possible_diagnoses = []
        for rule in rule_fact_mapping:
            disease = rule["disease"]
            rule_facts = rule["facts"]
            match_count = 0
            total_facts = len(rule_facts)
            matching_facts = []  # To store the matched facts for reasoning

            for key, value in rule_facts.items():
                if key in input_facts:
                    if isinstance(value, list):
                        if input_facts[key] in value:
                            match_count += 1
                            matching_facts.append(f"{key}: {input_facts[key]}")
                    elif input_facts[key] == value:
                        match_count += 1
                        matching_facts.append(f"{key}: {input_facts[key]}")

            confidence = (match_count / total_facts) * 100
            if confidence > 0:
                possible_diagnoses.append({
                    "disease": disease,
                    "confidence": confidence,
                    "reasoning": matching_facts,
                })

        # Debugging: Print possible diagnoses
        print("Possible diagnoses:", possible_diagnoses)

        # Build the output with reasoning
        if possible_diagnoses:
            output = "No exact match found. Possible diagnoses are:\n"
            for diagnosis in sorted(possible_diagnoses, key=lambda x: x["confidence"], reverse=True):
                reasoning_str = "\n  ".join([f"- {fact}" for fact in diagnosis["reasoning"]])
                output += f"\n- {diagnosis['disease']} ({diagnosis['confidence']:.2f}% confidence):\n  Based on the following matched facts:\n  {reasoning_str}\n"
        else:
            output = "No matching diseases could be found based on the provided symptoms."

        # Debugging: Print final output
        print("Output:", output)

        # Set result
        self.result = output

    def declare(self, fact):
        """
        Override declare method to track matched rules and support more flexible matching
        """
        result = super().declare(fact)
        return result