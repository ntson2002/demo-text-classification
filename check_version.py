#!/usr/bin/env python3
"""
Script to check installed package versions and update requirements.txt
"""

import subprocess
import sys

# List of packages to check
packages = [
    'transformers',
    'datasets',
    'accelerate',
    'torch',
    'evaluate',
    'scikit-learn'
]

def get_package_version(package_name):
    """Get the installed version of a package"""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'show', package_name],
            capture_output=True,
            text=True,
            check=True
        )
        
        for line in result.stdout.split('\n'):
            if line.startswith('Version:'):
                return line.split(':', 1)[1].strip()
        return None
    except subprocess.CalledProcessError:
        return None

def main():
    print("Checking installed package versions...\n")
    
    requirements = []
    
    for package in packages:
        version = get_package_version(package)
        if version:
            print(f"✓ {package}: {version}")
            requirements.append(f"{package}=={version}")
        else:
            print(f"✗ {package}: Not installed")
            requirements.append(f"# {package}==<NOT_INSTALLED>")
    
    # Write to requirements.txt
    output_file = 'requirements.txt'
    with open(output_file, 'w') as f:
        f.write('\n'.join(requirements))
        f.write('\n')
    
    print(f"\n✓ Requirements saved to {output_file}")
    print("\nContents of requirements.txt:")
    print("-" * 40)
    with open(output_file, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()