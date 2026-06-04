import ast
import os
import sys

def get_imports(directory):
    imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    try:
                        tree = ast.parse(f.read(), filename=path)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    imports.add(alias.name.split('.')[0])
                            elif isinstance(node, ast.ImportFrom):
                                if node.module:
                                    imports.add(node.module.split('.')[0])
                    except Exception as e:
                        print(f"Failed to parse {path}: {e}")
    return imports

def get_requirements(filepath):
    reqs = set()
    if not os.path.exists(filepath):
        return reqs
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                reqs.add(line.split('==')[0].split('>')[0].split('<')[0].split('~')[0].lower())
    return reqs

# Standard libs to ignore
STDLIB = {'os', 'sys', 'ast', 'math', 'json', 'datetime', 're', 'collections', 'typing', 'itertools'}

def main():
    if len(sys.argv) < 3:
        print("Usage: check_reqs.py <src_dir> <requirements.txt>")
        sys.exit(1)
        
    src_dir = sys.argv[1]
    req_file = sys.argv[2]
    
    imports = get_imports(src_dir)
    reqs = get_requirements(req_file)
    
    # Filter out stdlib and local modules
    imports = {imp for imp in imports if imp not in STDLIB}
    
    # Very simple normalization for comparison
    imports_norm = {imp.lower().replace('_', '-') for imp in imports}
    reqs_norm = {req.lower().replace('_', '-') for req in reqs}
    
    # Check for missing
    missing = []
    for imp in imports_norm:
        if imp not in reqs_norm and imp != "src":
            missing.append(imp)
            
    if missing:
        print(f"ERROR: Missing requirements for imports: {', '.join(missing)}")
        sys.exit(1)
    else:
        print("All imports are satisfied by requirements.txt")
        sys.exit(0)

if __name__ == '__main__':
    main()
