def classify_lien(text):

    text = text.lower()

    results = {
        "owelty": False,
        "heloc": False,
        "renewal_extension": False,
        "cash_advance": False
    }

    # Owelty Detection
    if "owelty" in text:
        results["owelty"] = True

    # HELOC Detection
    if "home equity line of credit" in text:
        results["heloc"] = True

    # Renewal & Extension
    if "renewal and extension" in text:
        results["renewal_extension"] = True

    # Cash Advance
    if "cash advance" in text:
        results["cash_advance"] = True

    return results

def calculate_risk(results):

    if results["cash_advance"]:
        return "HIGH"

    if results["heloc"]:
        return "MEDIUM"

    return "LOW"

