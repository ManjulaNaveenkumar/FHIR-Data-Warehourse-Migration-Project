# RMHC CSV to FHIR Warehouse
> Academic project demonstrating CSV-to-FHIR transformation using HAPI FHIR and Docker.

## Overview
This project demonstrates the transformation of legacy CSV healthcare data into a live, stateful FHIR Warehouse using a HAPI FHIR R4 server.

---

## Infrastructure – The Container Advantage
Docker was used to deploy the HAPI FHIR server, eliminating dependency issues related to Java and databases. Port mapping (8081 → 8080) allows the containerized server to be accessed from the host machine.

---

## Rulebook – Semantic Integrity
FHIR follows an 80/20 philosophy and is intentionally flexible. To ensure semantic consistency, a local Patient profile was created using FHIR Shorthand (FSH), enforcing mandatory fields like gender and birthDate.

---

## Translator – From Flat Files to Semantics
Legacy CSV data was translated into FHIR Patient resources using Python. Magic strings such as "M/F" were normalized to FHIR-compliant values ("male/female") using a mapping approach similar to ConceptMap.

---

## Transactional Safety
The architecture supports transactional ingestion, ensuring no orphaned clinical data and preserving referential integrity in the FHIR server.

---

## Outcome
Instead of generating inert JSON files, this project results in a live, queryable FHIR server that enforces validation and supports scalable healthcare interoperability.
