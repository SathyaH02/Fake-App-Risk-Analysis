def classify(score):
    if score > 0.85:
        return "High Risk"
    if score > 0.6:
        return "Medium Risk"
    return "Low Risk"
