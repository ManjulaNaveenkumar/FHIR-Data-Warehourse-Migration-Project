Profile: SimpleObservationProfile
Parent: Observation
Description: "A simple Observation profile capturing vital signs or lab results"

* status 1..1 MS
* category 0..* 
  // Example: vital-signs, laboratory
* code 1..1 MS
  // The type of observation, e.g., blood pressure, hemoglobin
* subject 1..1 MS
  // Reference to Patient
* effectiveDateTime 0..1
  // When the observation was taken
* valueQuantity 0..1
  // Numeric value for lab result or measurement
* interpretation 0..1
  // Optional interpretation, e.g., normal/abnormal
  