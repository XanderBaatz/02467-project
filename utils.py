import gender_guesser.detector as gender

# Gender detector
d = gender.Detector()

def classify_gender(name):
    # Initial guess
    g = d.get_gender(name=name)

    if g != "unknown":
        return g
    
    # Fallback heuristic
    if name[-1].lower() in "aeiouy": # if last character in name is a vowel it's likely female
        return "female"
    elif name[-1].lower() in "korst": # if last character in name is one of these, it's likely male
        return "male"
    else:
        return "unknown"

