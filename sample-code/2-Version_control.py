###
# -----------------------------------------------------------------------
# 2. Version Control: Implement version control for your features to
# track changes over time. This facilitates model reproducibility and
# allows rollback to previous versions if needed, enhancing model
# governance and auditability.
# -----------------------------------------------------------------------
###

# AWS Feature Store does not support traditional version control like Git. However, you can manage versions by tracking changes through the use of multiple feature groups or appending version indicators to feature names:

feature_group_v2 = FeatureGroup(name='my-feature-group-v2', sagemaker_session=session)
# ----- Hopsworks
# Supports versioning directly in feature store
# Create a new version of an existing feature group
featurestore.create_featuregroup(
    data=new_version_df,
    featuregroup_name='my_feature_group',
    description='Updated feature group for ML models',
    version=2
)
