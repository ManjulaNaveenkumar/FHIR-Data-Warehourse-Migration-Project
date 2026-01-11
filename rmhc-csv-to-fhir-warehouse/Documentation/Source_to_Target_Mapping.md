# Source to Target Mapping (STM)

| CSV Column  | Meaning              | FHIR Resource | FHIR Element        |
|------------|----------------------|--------------|---------------------|
| patient_id | Legacy Patient ID     | Patient      | Patient.identifier  |
| gender     | M / F codes           | Patient      | Patient.gender      |
| dob        | Date of Birth         | Patient      | Patient.birthDate   |
| last_name | Patient Last Name     | Patient      | Patient.name.family |

Gender values are normalized using a ConceptMap approach:
- M → male
- F → female
