import re

text_to_use = """
email e.nsengiman@alustudent.com , Ishema.kenny@alustudent.uni.rw
website https://www.example.com , https://subdomain.example.org/page
phone (250) 787-4581, 256-456-7890 or 254.017.7890
credit cards: 1234 5678 9012 3456 and 1234-5678-9012-3456
"""
patterns = {
    "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "URLs": r"https?://[^\s]+",
    "Phone Numbers": r"(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}",
    "Credit Cards": r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
}

def extract_data(patterns, text):
    results = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        results[key] = matches
    return results

results = extract_data(patterns, text_to_use)

for category, matches in results.items():
    print(f"{category} Found:")
    for match in matches:
        print(f" - {match}")
    print()
