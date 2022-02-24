# Description
 A simple CLI application that makes jfrog-artifactory API calls

## Requirements
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)

## Getting started

First, make sure you have all the required tools installed on your local machine then continue with these steps.

# Steps to reproduce
  Steps to pull the project through the artifactory:
  
  1.)	Go to https://danielabergelassignment.jfrog.io/
  
  2.)	Enter a username and password
  
  •	Username = <yourusername>
                                                  
  •	Password = <yourpassword>
  
  
  3.)	Go to Packages under Artifactory tab, There you can see the project I wrote in python and put it in docker
  4.)	Click on saas-api packages and click the latest version.
  5.)	Copy this command in your terminal or cmd: ```docker pull danielabergelassignment.jfrog.io/saas-docker-local/saas-api:latest```
  6.)	After the docker has finished to pull the entire image use that command:
  ```docker run -it --name my_app --rm danielabergelassignment.jfrog.io/saas-docker-local/saas-api```
  7.)	Now that we're inside the downloaded image we can write down this command to run the project : ```python main.py –-help```
  8.)	These are all the flags that the app supports:
  ** Flag	                  ** Description
  -h, --help            	show this help message and exit
  --ping                	Sends a ping request
  --storageinfo	Returns storage summary information regarding binaries, file store and repositories.
  --repolist            	Returns a list of minimal repository details for all repositories of the specified type.
  -v, --version	Retrieve information about the current Artifactory version.
  --deleteuser	[Username Required] This API will delete a single user.

  
  Link to GitHub repo: https://github.com/danizz91/saas-API  
    
