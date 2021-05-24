import os
import re
import zipfile
import subprocess
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


def extract_artifact(dir_name, zip_file_name):
    zip_ref = zipfile.ZipFile(zip_file_name)
    zip_ref.extractall(dir_name)
    zip_ref.close()
    os.remove(zip_file_name)


val = "Value"
num = 5
