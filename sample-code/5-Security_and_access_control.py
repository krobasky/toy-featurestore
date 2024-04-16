###
# -----------------------------------------------------------------------
# 5. Security and Access Control: Secure access to the feature store,
# especially if it contains sensitive or proprietary data. Use
# role-based access controls to ensure that only authorized users and
# systems can access or modify the features.
# -----------------------------------------------------------------------
###

# Use AWS IAM policies and resource-based policies to control access to your feature groups:

import boto3

iam = boto3.client('iam')
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sagemaker:GetRecord",
            "Resource": "arn:aws:sagemaker:region:account-id:feature-group/my-feature-group"
        }
    ]
}
iam.put_role_policy(RoleName='MySageMakerRole', PolicyName='FeatureStoreAccess', PolicyDocument=json.dumps(policy))
# ----- Hopsworks
# Built-in security and fine-grained access control to manage who can access feature groups:
# Use Hopsworks' project-based multi-tenancy and user roles to control access
# Here is a conceptual example; specific API might differ
hopsworks.set_permissions(featuregroup_name='my_feature_group', version=1, permission_level='read_only', user='data_scientist')

