
import requests
import json


def sendPingRequest(baseURL, headers):
    url = baseURL + '/access/api/v1/system/ping'
    headers["content-type"] = "text/plain"

    try:
        response = requests.get(url, headers=headers)
        if (response):
            return {"status_code": response.status_code, "message": response.text}
        else:
            return "An error occured"
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def storageSummaryRequest(baseURL,headers):
    url = baseURL + '/artifactory/api/storageinfo'

    try:
        response = requests.get(url,headers=headers)
        if(response and response.status_code == 200):
            return {'status_code': response.status_code, "message": json.loads(response.text)}
        else:
            return 'Error there is no response back'
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def repositoriesListRequest(baseURL,headers):
    url = baseURL + '/artifactory/api/repositories?type=local'

    try:
        response = requests.get(url,headers=headers)
        if(response):
            return {'status_code': response.status_code, "message": json.loads(response.text)}
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def getVersion(baseURL,headers):
    url = baseURL + '/artifactory/api/system/version'

    try:
        response = requests.get(url,headers=headers)
        if(response):
            return json.loads(response.text)["version"]
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def deleteUser(baseURL,headers,username):
    url = baseURL + f"/artifactory/api/security/users/{username}"

    try:
        response = requests.delete(url,headers=headers)
        if(response):
            return {'status_code': response.status_code, "message": response.text}
        else:
            return 'User not found'
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
