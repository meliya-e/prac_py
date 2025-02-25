import os
import sys
import zlib

def get_git_directory(repo_path):
    git_dir = os.path.join(repo_path, '.git')
    return git_dir if os.path.exists(git_dir) else None

def list_branches(repo_path):
    git_dir = get_git_directory(repo_path)
    if not git_dir:
        print("not a valid git repository")
        return
    
    heads_dir = os.path.join(git_dir, 'refs', 'heads')
    if not os.path.exists(heads_dir):
        print("No branches found!")
        return
    
    for branch in os.listdir(heads_dir):
        print(f"{branch}")

def read_git_object(repo_path, sha):
    obj_path = os.path.join(repo_path, '.git', 'objects', sha[:2], sha[2:])
    try:
        with open(obj_path, 'rb') as f:
            return zlib.decompress(f.read())
    except FileNotFoundError:
        print(f"Git object {sha} not found")
        sys.exit(1)

def parse_commit(data):
    parts = data.decode("utf-8", errors="replace").split("\n\n", 1)
    header = parts[0].splitlines()
    message = parts[1].strip() if len(parts) > 1 else ""
    
    commit_data = {"message": message, "parents": []}
    for line in header:
        key, _, value = line.partition(" ")
        if key == "tree":
            commit_data["tree"] = value
        elif key == "parent":
            commit_data["parents"].append(value)
        elif key == "author":
            commit_data["author"] = value
        elif key == "committer":
            commit_data["committer"] = value
    
    return commit_data

def show_last_commit(repo_path, branch_name):
    branch_path = os.path.join(repo_path, '.git', 'refs', 'heads', branch_name)
    if not os.path.exists(branch_path):
        print(f"Branch '{branch_name}' not found")
        return None, None
    
    with open(branch_path, 'r') as f:
        commit_sha = f.read().strip()
    
    data = read_git_object(repo_path, commit_sha)
    commit_data = parse_commit(data.split(b'\x00', 1)[1])
    
    print(f"Commit {commit_sha}")
    print(f"Tree: {commit_data.get('tree', '')}")
    for parent in commit_data.get("parents", []):
        print(f"Parent: {parent}")
    print(f"Author: {commit_data.get('author', '')}")
    print(f"Committer: {commit_data.get('committer', '')}\n")
    print(commit_data.get("message", ""))
    
    return commit_data, commit_sha

def parse_tree(content):
    entries = []
    pos = 0
    while pos < len(content):
        space_idx = content.index(b" ", pos)
        mode = content[pos:space_idx].decode()
        pos = space_idx + 1
        null_idx = content.index(b"\x00", pos)
        filename = content[pos:null_idx].decode()
        pos = null_idx + 1
        sha = content[pos:pos + 20].hex()
        pos += 20
        typ = "tree" if mode == "40000" else "blob"
        entries.append((typ, filename, sha))
    return entries

def show_tree(repo_path, tree_sha):
    data = read_git_object(repo_path, tree_sha)
    entries = parse_tree(data.split(b'\x00', 1)[1])
    for mode, filename, sha in entries:
        print(f"{mode} {sha} {filename}")

def show_history(repo_path, commit_data, commit_sha):
    while commit_sha:
        print(f"TREE for commit {commit_sha}")
        show_tree(repo_path, commit_data["tree"])
        
        if commit_data["parents"]:
            commit_sha = commit_data["parents"][0]
            data = read_git_object(repo_path, commit_sha)
            commit_data = parse_commit(data.split(b'\x00', 1)[1])
        else:
            break

if len(sys.argv) < 2:
    print("use: python prog.py arg1 arg2")
    sys.exit(1)
    
repo_path = sys.argv[1]
if len(sys.argv) == 2:
    list_branches(repo_path)
else:
    commit_data, commit_sha = show_last_commit(repo_path, sys.argv[2])
    if commit_data:
        show_history(repo_path, commit_data, commit_sha)

