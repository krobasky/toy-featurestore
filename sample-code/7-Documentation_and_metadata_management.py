###
# -----------------------------------------------------------------------
# 7. Documentation and Metadata Management (eliminate tribal
# knowledge): Maintain comprehensive documentation and metadata for
# each feature, including its source, transformation logic,
# dependencies, and usage guidelines. This improves usability and
# helps new team members discover, understand and leverage the feature
# store effectively.
# -----------------------------------------------------------------------
###

# Manage metadata by embedding descriptions within your feature store definitions or using external systems like AWS Glue:

# Add descriptions to your feature definitions (not directly supported, but assume metadata handling)
feature_group = FeatureGroup(name='my-feature-group', sagemaker_session=session, description="This feature group contains...")
# ----- Hopsworks
# Documenting a feature group during creation
featurestore.create_featuregroup(
    data=my_dataframe,
    featuregroup_name='my_feature_group',
    description='Feature group with extensive metadata for tracking.',
    version=4
)
# Accessing feature group metadata
metadata = featurestore.get_featuregroup_metadata('my_feature_group', version=4)
print(metadata)
