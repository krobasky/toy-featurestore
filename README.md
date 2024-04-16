# toy-featurestore
Example code for feature store best practices

## Purpose

This project has been created for demonstrating code to implement a Feature Store.

## Assumptions

The following assumptions were made for implementing the demonstration under sample-code:

 - System requirements: **Snowflake** and **SageMaker**
 - Feature Store technology preferences: none
 - Security: Feature Store access will be kept behind a company firewall on a private VPC; no requirement for exposure
 - Scale: Petabytes scaling towards exabyte level data lake
 - Budget and performance constraints: typical
 - Feature rate of change: typical
 - Edge deployments: Assuming not required short term, but longer term may be desirable

## Manifest

The directory contains the following files:

<pre>
.
├── LICENSE: Permissive license
├── README.md: This file
└── sample-code: directory of sample code demonstrating best practices
    ├── 1-Centralization.py
    ├── 2-Version_control.py
    ├── 3-Scalability_and_performance.py
    ├── 4-Data_quality_and_monitoring.py
    ├── 5-Security_and_access_control.py
    ├── 6-Integration_with_ML_workflow.py
    └── 7-Documentation_and_metadata_management.py
</pre>
