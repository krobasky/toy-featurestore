###
# -----------------------------------------------------------------------
# 6. Integration with ML Workflow (better predictions): Integrate the
# feature store seamlessly with your existing machine learning
# pipelines and data sources. Ensure that features are fresh (not a
# day old) and support both batch processing for model training and
# real-time processing (10ms response time) for inference.
# -----------------------------------------------------------------------
###

# how you might use a feature store during model training in SageMaker:

from sagemaker.inputs import TrainingInput

training_job = sagemaker.estimator.Estimator(...)
training_job.fit({'train': TrainingInput(s3_data='s3://my-bucket/my-feature-store/train/', 
                                         feature_group_arn='arn:aws:sagemaker:region:account-id:feature-group/my-feature-group')})

# ----- Hopsworks
# Assuming the Hopsworks Feature Store is accessible from SageMaker
from hops import featurestore
import sagemaker

# Get training data from Hopsworks Feature Store
train_data = featurestore.get_featuregroup('my_feature_group', version=1)

# Convert to CSV, upload to S3, and use it in a SageMaker Estimator
train_data.write.csv('s3://my-bucket/train_data.csv')
sagemaker_estimator = sagemaker.estimator.Estimator(...)
sagemaker_estimator.fit('s3://my-bucket/train_data.csv')
