# AWS Continuous Integration Demo

## Set Up GitHub Repository

The first step in our CI journey is to set up a GitHub repository to store our Python application's source code. If you already have a repository, feel free to skip this step. Otherwise, let's create a new repository on GitHub by following these steps:

- Go to github.com and sign in to your account.
- Click on the "+" button in the top-right corner and select "New repository."
- Give your repository a name and an optional description.
- Choose the appropriate visibility option based on your needs.
- Initialize the repository with a README file.
- Click on the "Create repository" button to create your new GitHub repository.

Great! Now that we have our repository set up, we can move on to the next step.

### Step 1: Set Up Your Code Repository

1. **Choose a Repository**:
   - You can use AWS CodeCommit, GitHub, GitLab, or Bitbucket as your source repository.
   - Ensure your repository contains the necessary code and a buildspec.yml file, which defines the build commands and settings for CodeBuild.

2. **Create a buildspec.yml File**:
   - This YAML file specifies the commands to run at each phase of the build process. For a UI project, you might include commands to install dependencies, run tests, and build the application.

   Example buildspec.yml for a React project:
   ```yaml
   version: 0.2

   phases:
     install:
       commands:
         - npm install
     build:
       commands:
         - npm run build
   artifacts:
     files:
       - '**/*'
     base-directory: build
   ```

### Step 2: Create an AWS CodeBuild Project

1. **Navigate to CodeBuild in the AWS Console**:
   - Go to the AWS Management Console and navigate to CodeBuild under the "Developer Tools" section.

2. **Create a New Build Project**:
   - Click on the "Create build project" button.

3. **Project Configuration**:
   - **Project Name**: Enter a name for your project.
   - **Description**: Optionally, provide a description.

4. **Source**:
   - **Source Provider**: Select your source repository provider (e.g., GitHub, CodeCommit).
   - **Repository**: Select or connect your repository and provide repository URL.
   - **Branch/Tag**: Specify the branch or tag to build from. example: main

5. **Environment**:
   - **Environment Image**: Choose an image, either managed images(preffered) or custom docker image
   - **Operating system OS** Amzon linux or ubuntu or windows server (choose ubuntu or as per company requiremnet)
   - Runtime: Standard (of ubuntu)
   - Image: choose latest image(of ubuntu)
**when you are using Jenkins what you usually do is you create worker nodes and on top of the worker nodes you install some operating system or you say Jenkins that run the Jenkins pipelines on this environment but here environement is provided by AWS.
   - Environment Type: Linux  

   - **Service Role**: You can either create a new service role or use an existing one. The service role allows CodeBuild to interact with other AWS services on your behalf.(Example: it needs to connect with system manager where secret credentials are kept)

6. **Buildspec**:
   - You can either use a buildspec file from your source repository (e.g., buildspec.yml) or define the commands directly in the console(insert build command).
   - if using build commands, it is very easy as you just have to uncomment what you require (and you can copy the code and save root of your source code repo as buildspec.yml) 

7. **Artifacts**:
   - **Type**: Choose where to store the build output (e.g., Amazon S3).
   - **Bucket Name**: Select an S3 bucket to store the build artifacts.

8. **Logs**:
   - You can enable CloudWatch logs or S3 bucket logging to monitor build details.

9. **Additional Configuration**:
   - Set any additional options, such as environment variables, VPC configurations, or build timeouts.

>>Click on create build project.

### Step 3: Build and Test

1. **Start a Build**:
   - After setting up the project, you can start a build manually from the CodeBuild console or set up a trigger (e.g., when changes are pushed to the repository).

2. **Monitor the Build**:
   - You can monitor the build process in the CodeBuild console, where logs will be displayed in real-time.

3. **Artifacts and Outputs**:
   - Once the build is complete, the artifacts (e.g., the built UI application) will be stored in the specified S3 bucket or another storage solution.

## Create an AWS CodePipeline
In this step, we'll create an AWS CodePipeline to automate the continuous integration process for our Python application. AWS CodePipeline will orchestrate the flow of changes from our GitHub repository to the deployment of our application. Let's go ahead and set it up:

- Go to the AWS Management Console and navigate to the AWS CodePipeline service.
- Click on the "Create pipeline" button.
- Provide a name for your pipeline and click on the "Next" button.
- For the source stage, select "GitHub(version 2 or above)" as the source provider.
- Connect to your GitHub account(pop-up>>provide any connection name>> select/serch your github accoutand connect ) to AWS CodePipeline and select your repository.
- Choose the branch you want to use for your pipeline.
- In the build stage, select "AWS CodeBuild" as the build provider.(AWS support Jenkins also)
- select your already created code build project or Create a new CodeBuild project by clicking on the "Create project" button. then select build type as single build(preffered) or Batch Build.>> click next
- Deploy Provider >> select Code deploy >> next>> verify and create pipeline


## Trigger the CI Process

In this final step, we'll trigger the CI process by making a change to our GitHub repository. Let's see how it works:

- Go to your GitHub repository and make a change to your Python application's source code. It could be a bug fix, a new feature, or any other change you want to introduce.
- Commit and push your changes to the branch configured in your AWS CodePipeline.
- Head over to the AWS CodePipeline console and navigate to your pipeline.
- You should see the pipeline automatically kick off as soon as it detects the changes in your repository.
- Sit back and relax while AWS CodePipeline takes care of the rest. It will fetch the latest code, trigger the build process with AWS CodeBuild, and deploy the application if you configured the deployment stage.



