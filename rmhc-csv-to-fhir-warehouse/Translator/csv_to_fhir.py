# Sample CSV to FHIR translator
# Academic demonstration using anonymized data

import csv
import json

gender_map = {
    "M": "male",
    "F": "female"
}

with open("sample_rmhc_data.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        patient_resource = {
            "resourceType": "Patient",
            "identifier": [{
                "system": "http://example.org/rmhc/patient-id",
                "value": row["patient_id"]
            }],
            "name": [{
                "family": row["last_name"]
            }],
            "gender": gender_map.get(row["gender"], "unknown"),
            "birthDate": row["dob"]
        }

        print(json.dumps(patient_resource, indent=2))
