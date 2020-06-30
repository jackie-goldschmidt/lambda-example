## Lambda Example
Simple example of a step function that invokes a lambda.

For more information, see the Readme.MD inside the lambda-example directory.

To run in a container
```
sam build --use-container
sam local invoke SayHelloFunction --event events/event.json
```

To deploy
```
sam build --use-container
sam deploy --region us-east-2 \
--s3-bucket="aws-sam-cli-managed-default-samclisourcebucket-1fcp8pqgpawmn" \
--stack-name="say-hello" \
--capabilities="CAPABILITY_IAM"

```
