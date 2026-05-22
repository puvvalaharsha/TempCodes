import csv

keywords = [
    "SephoraSameDayUnlimitedModalPage",
    "SubscribeToSephoraModal",
    "mySephoraSection",
    "HappeningSephoraMainPage",
    "clickSephoraLogo",
    "SephoraCreditCardApplicationFormPage",
    "SEPHORA_CREDIT_CARD_PROGRAM_LINK_NAME",
    "com.sephora",
    "com.sephora.appmodules",
    "com.sephora.enterprise.sephoramobile"
]

with open("sephora_keywords.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Keyword"])

    for index, keyword in enumerate(keywords, start=1):
        writer.writerow([index, keyword])

print("CSV file generated successfully.")
