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
                # Convert Fact object to a readable string format
                fact_str = ", ".join([f"{key}: {value}" for key, value in fact.items()])
                matched_facts.append(fact_str)

        # Build the diagnostic explanation
        matched_facts_str = "\n".join([f"- {fact}" for fact in matched_facts])
        reasoning = f"""Diagnosis: {disease}

    Diagnostic Explanation:
    This diagnosis is based on the following facts:
    {matched_facts_str} 
    """
        self.result = reasoning

    def declare(self, fact):
        """
        Override declare method to track matched rules and support more flexible matching
        """
        result = super().declare(fact)
        return result