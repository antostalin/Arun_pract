##Deploying Java API application into AWS environment
This application is going to deploy the code into AWS environment by creating the build environment and pipeline from the GitHub repository then deploy the code into EC2 instance. Also create the `buildspec.yml` file to define the steps to compile and deploy the code and this build pipeline will be executed for any changes happened to the GitHub repository as well as deploy the latest code changes into the EC2 instance to immediately reflect the changes while accessing the API endpoints.

###Creating spring-boot web application
- Create the `order-service` spring-boot application
- Run the application in your local environment and make sure the application was running as expected
- This spring-boot web application was exposed through http://localhost:5000 url
- The API exposed from this web-application as
  - `/orders` -- it will list out the product list which was ordered
  - `/orders/sorted` -- it will list out the product based on price in ascending order

If above steps are done then we are good to proceed with next step.
  
###Check-in the code changes into GitHub

###Configuring the CodeBuild and Deployment to AWS

###Validating changes deploy to AWS 