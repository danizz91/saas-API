import argparse
import helpers


if __name__ == '__main__':
    #The IP of the internal app
    baseURL = 'https://danielabergelassignment.jfrog.io'
    #set-up the header with authorization and content-type headers
    headers = {
        'content-type': 'application/json',
        'authorization': 'Bearer eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiJ3T3lBSkJBZ0J6ZndSR3BrUVBXX2llUEZkLVJCT2FqYjlUa25uQWx1eXBnIn0.eyJleHQiOiJ7XCJyZXZvY2FibGVcIjpcInRydWVcIn0iLCJzdWIiOiJqZmFjQDAxZnc5c2FmNGp6YTh5MTlqZWptNnMwdno4XC91c2Vyc1wvZGFuaWVsenoiLCJzY3AiOiJhcHBsaWVkLXBlcm1pc3Npb25zXC9hZG1pbiIsImF1ZCI6IipAKiIsImlzcyI6ImpmZmVAMDAwIiwiZXhwIjoxNjc3MTc4NTU3LCJpYXQiOjE2NDU2NDI1NTcsImp0aSI6ImYyYjcxNDk1LTM1OTgtNDdlZC1iMGRhLTNmMDg0YjYxNDI3NCJ9.W9HoQjGLoW5BdCx4XfwPZH7hHHps9y5ceiBjE9v4itlVO8ticiJXvc1L9VAQ6uNtX__f6q4xnH_IdqzUqqJkoGSYNUUYp2xo5S2LMSK-gAzXKTWZhXCU3R5wmw9reOrNQ5vMXmnrn8Cuihqd67VUSdIomk6wxCEMtZnwELwGyJp0KkRQF1iOLFVvV8VXswWB8dbKzoQIcSUrvQFB3j6FqQOhbdxojnzmrvENQoejdUfmXBvSr4My5F9EGh0G4VQEZ6xwsbTpUpYDxGr1JIXVsnk30h5kYpvmyqE51r8mL21fwpahTl8ieNCNZInGo-o9qWVSvllCF7kzgBtfyYGhXw'
    }

    parser = argparse.ArgumentParser(description='Some API calls being tested against the local jfrog application')
    parser.add_argument('--ping', help='Sends a ping request',action='store_true')
    parser.add_argument('--storageinfo',help='Returns storage summary information regarding binaries, file store and repositories.',action='store_true')
    parser.add_argument('--repolist',help='Returns a list of minimal repository details for all repositories of the specified type.',action='store_true')
    parser.add_argument('-v','--version',help='Retrieve information about the current Artifactory version.',action='store_true')
    parser.add_argument('--deleteuser',dest='username',help='This API will delete a single user. [Provide a username]')




    args = parser.parse_args();

    if args.ping:
        #Sends a ping request with authorization header, Using GET method
        print(helpers.sendPingRequest(baseURL,headers))
    elif args.storageinfo:
        #Sends request to the API and returns JSON with the amount of utilization of the system, Using GET method
        print(helpers.storageSummaryRequest(baseURL,headers))
    elif args.repolist:
        #Sends request with parameter to the API and returns JSON list of repositories which are local, Using GET method
        print(helpers.repositoriesListRequest(baseURL,headers))
    elif args.version:
        #Sends request to the API and pulling the version, Using GET method
        print(helpers.getVersion(baseURL,headers))
    elif args.username:
        #Sends request to the API and deletes it if it is in the system, Using Delete method
        print(helpers.deleteUser(baseURL,headers,args.username))
