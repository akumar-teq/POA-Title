from app.services.lien_classifier import classify_lien

sample_text = """

THIS IS AN OWELTY OF PARTITION AGREEMENT

HOME EQUITY LINE OF CREDIT

"""

result = classify_lien(sample_text)

print(result)
