import sys
import os
import re
import zipfile
import base64
import subprocess
import requests
import json
import socket

def get_query_string(deploy_script_name):
    querystring = {
        "$filter": "name like '" + deploy_script_name + "'"
    }
    return querystring


def get_unittest_query_string(test_script_name):
    unit_test_querystring = {
        "scriptname": test_script_name
    }
    return unit_test_querystring


def get_repo_dir():
    repo_dir = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                                stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
    return repo_dir


def is_branch():
    hostname = socket.gethostname()
    if hostname != 'ecs-1ad179aa':
        current_branch = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                                          stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
    else:
        current_branch = subprocess.Popen(['git', 'branch', '-r'],
                                          stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8').lstrip(
            " origin/")
    return current_branch


def get_commit_hash():
    commit_id = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                                 stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
    return commit_id


def get_delta_files(current_commit_sha):
    committed_files = subprocess.Popen(['git', 'diff-tree', '--no-commit-id', '--name-status', '-r', current_commit_sha],
                                       stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
    changed_scripts = open('commit.log', 'w')
    changed_scripts.writelines(committed_files)
    changed_scripts.close()
    file = "commit.log"
    f = open(file, "r")
    lines = f.readlines()
    result = []
    for x in lines:
        result.append(x.split())
    f.close()
    scripts = []
    for i in range(len(result)):
        if result[i][0] == "M" or result[i][0] == "A":
            scripts.append(result[i][1])
        else:
            continue
    # remove commit log file
    os.remove('commit.log')
    return scripts


def get_deploy_files(file_list, path_pattern_cpq_repo):
    deploy_scripts = []
    for filename in file_list:
        if re.search(path_pattern_cpq_repo, filename, re.I):
            deploy_scripts.append(filename)
        else:
            continue
    return deploy_scripts


def get_extension(cpq_file_name):
    extension = os.path.splitext(cpq_file_name)[1]
    return extension


def get_file_name(path_with_file_name):
    filename_without_path = os.path.basename(path_with_file_name)
    return filename_without_path


def get_file_basename(dot_extension, filename):
    file_basename = ""
    if dot_extension == ".py" or dot_extension == ".html":
        file_basename = filename.rstrip(dot_extension)
    else:
        print("no files with extension .py or .html")
    return file_basename


def get_script_content(script_name_with_path):
    script_file = open(script_name_with_path, "r")
    content = script_file.read()
    return content


# def script_content(script_path):
#     script_file = open(script_path, "r")
#     content = script_file.read()
#     return content


def get_token(domain_payload):
    response = requests.request("POST", token_url, data=domain_payload, headers=None)
    json_data = json.loads(response.text)
    data = dict(json_data)
    access_token = data["access_token"]
    access_type = data["token_type"]
    bearer_key = str(access_type + " " + access_token)
    return bearer_key


def get_gs_payload(gs_script_name, file_content):
    payload = {
        "scriptDefinition": {
            "Name": gs_script_name,
            "SystemId": gs_script_name + "_cpq",
            "Active": True,
            "script": file_content
        }
    }
    return payload


def get_ca_payload(ca_script_name, file_content):
    custom_payload = {
        "actionDefinition": {
            "name": ca_script_name,
            "placement": "C",
            "SystemId": ca_script_name + "_cpq",
            "actionDisplayLevel": True,
            "script": file_content
        },
        "actionCondition": {
            "globalCondition": "",
            "preActionCondition": "",
            "postActionCondition": ""
        }
    }
    return custom_payload


def get_rt_payload(rt_template_name, file_content):
    template_payload = {
            "Name": rt_template_name,
            "TemplateId": 23,
            "description": "",
            "isDefault": False,
            "content": file_content,
            "SystemId": rt_template_name + "_cpq"

    }
    return template_payload


def get_unit_test_payload(content, unit_test_script_basename):
    ut_payload = {
        "script": content,
        "script_name": unit_test_script_basename
    }
    return ut_payload


def get_script_cpq(method, url, headers, querystring):
    response = requests.request(method, url, headers=headers, params=querystring)
    data = dict(json.loads(response.text))
    scripts = []
    script_name = ""
    script_id = ""
    if data["totalNumberOfRecords"] == 0:
        print("User Script is New")
        script_name = ""
        script_id = ""
    elif data["totalNumberOfRecords"] == 1:
        print("User Script exists in CPQ list")
        if url == cpq_global_script_url:
            script_name = data["pagedRecords"][0]["scriptDefinition"]["name"]
            script_id = data["pagedRecords"][0]["scriptDefinition"]["id"]
        elif url == cpq_custom_action_url:
            script_name = data["pagedRecords"][0]["actionDefinition"]["name"]
            script_id = data["pagedRecords"][0]["actionDefinition"]["id"]
        elif url == cpq_custom_rt_url:
            script_name = data["pagedRecords"][0]["name"]
            script_id = data["pagedRecords"][0]["id"]
    else:
        print("No url received")
    scripts.append(script_name)
    scripts.append(script_id)
    return scripts


def deploy_script(url, usr_script, scripts, headers, payload):
    if usr_script in scripts:
        print(usr_script + " exists in CPQ")
        print("Executing PUT request....")
        url_script_id = scripts[1]
        url = url + str(url_script_id)
        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)
        print(response.status_code)
    else:
        print(usr_script + " Does not exist")
        print("Executing POST request....")
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.status_code)


def get_unit_test_header(url, headers):
    response = requests.request("POST", url, headers=headers)
    data = response.text
    json_object = dict(json.loads(data))
    json_data = json.dumps(json_object["token"], indent=2)
    new_token = json.loads(json_data)
    jwt_header = {
        'authorization': "Bearer " + new_token,
        'content-type': "application/json"
    }
    return jwt_header


def run_unit_test(url, payload, headers, querystring):
    test_response = requests.request("POST", url, data=str(payload), headers=headers,
                                     params=querystring)
    test_data = test_response.text
    test_object = dict(json.loads(test_data))
    test_json_data = json.dumps(test_object, indent=2)
    return test_json_data


def extract_artifact(dir_name, zip_file_name):
    zip_ref = zipfile.ZipFile(zip_file_name)
    zip_ref.extractall(dir_name)
    zip_ref.close()
    os.remove(zip_file_name)


val = "Value"
num = 5
