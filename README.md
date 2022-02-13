# file with heading

In order to excute these commands you have to go to the specific project folder to run the following commands:

serverless deploy    Deploy changes
sls deploy --verbose  gives the output text, while executing the command
serverless info      View deployed endpoints and resources
serverless invoke    Invoke deployed functions
serverless --help    Discover more commands
sls create --template aws-python --path hello-world-python
sls invoke -f hello -l
sls deploy --verbose
sls deploy function -f hello
sls logs -f hello -t
sls remove
