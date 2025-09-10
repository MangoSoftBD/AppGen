#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AppGenStudio - Integrated Development Environment (IDE)
ইনস্টলেশন এবং ডিস্ট্রিবিউশন স্ক্রিপ্ট
"""

import os
import sys
import platform
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop

# প্রোজেক্ট মেটাডেটা
PROJECT_NAME = "AppGenStudio"
PROJECT_VERSION = "1.0.0"
PROJECT_DESCRIPTION = "An Integrated Development Environment (IDE) for programmers"
PROJECT_LONG_DESCRIPTION = """
AppGenStudio is a powerful Integrated Development Environment that provides
a simple and efficient environment for writing, editing, compiling, and debugging code.

Features:
- Advanced code editor with syntax highlighting and auto-completion
- Multi-language support (Python, Java, C++)
- Built-in debugger with breakpoints and variable inspection
- Project management tools
- Customizable UI with dark and light themes
- Cross-platform support (Windows, Linux, macOS)
"""

PROJECT_AUTHOR = "Ashikur Rahaman"
PROJECT_AUTHOR_EMAIL = "mangolabbd@outlook.com"
PROJECT_URL = "https://github.com/MangoSoftBD/AppGenStudio"
PROJECT_LICENSE = "MIT"
PROJECT_KEYWORDS = ["ide", "editor", "development", "python", "java", "cpp"]

# ক্লাসিফায়ার্স
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Integrated Development Environments (IDE)",
    "Topic :: Text Editors",
    "Topic :: Utilities",
]

# ডিপেন্ডেন্সি
INSTALL_REQUIRES = [
    "PyQt5>=5.15.9",
    "pygments>=2.15.1",
    "click>=8.1.6",
    "pyyaml>=6.0",
    "watchdog>=3.0.0",
    "requests>=2.31.0",
    "psutil>=5.9.5",
]

# অপশনাল ডিপেন্ডেন্সি
EXTRAS_REQUIRE = {
    "dev": [
        "pytest>=7.4.0",
        "pytest-qt>=4.2.0",
        "pytest-cov>=4.1.0",
        "coverage>=7.3.0",
    ],
    "build": [
        "pyinstaller>=5.13.0",
        "wheel>=0.41.2",
    ],
}

# এন্ট্রি পয়েন্টস
ENTRY_POINTS = {
    "console_scripts": [
        "appgenstudio=src.main:main",
        "ags=src.main:main",
    ],
    "gui_scripts": [
        "AppGenStudio=src.main:main",
    ]
}

class PostInstallCommand(install):
    """ইনস্টলেশনের পরে এক্সট্রা সেটআপ"""
    def run(self):
        install.run(self)
        self._post_install()
    
    def _post_install(self):
        """ইনস্টলেশনের পরে রান হওয়া টাস্কস"""
        print("Running post-installation tasks...")
        
        # রিসোর্স ডিরেক্টরি তৈরি
        resources_dir = os.path.join(sys.prefix, 'share', 'appgenstudio')
        os.makedirs(resources_dir, exist_ok=True)
        
        # ডেস্কটপ শর্টকাট তৈরি (Windows)
        if platform.system() == "Windows":
            self._create_windows_shortcut()
        
        print(f"{PROJECT_NAME} {PROJECT_VERSION} installation completed successfully!")
    
    def _create_windows_shortcut(self):
        """Windows ডেস্কটপ শর্টকাট তৈরি"""
        try:
            import winshell
            from win32com.client import Dispatch
            
            desktop = winshell.desktop()
            shortcut_path = os.path.join(desktop, f"{PROJECT_NAME}.lnk")
            
            target = sys.executable
            wDir = os.path.dirname(sys.executable)
            icon = os.path.join(sys.prefix, "Lib", "site-packages", "appgenstudio", "resources", "icons", "app.ico")
            
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = target
            shortcut.Arguments = "-m src.main"
            shortcut.WorkingDirectory = wDir
            shortcut.IconLocation = icon
            shortcut.save()
            
            print(f"Desktop shortcut created: {shortcut_path}")
        except ImportError:
            print("Warning: Could not create desktop shortcut (required packages not installed)")
        except Exception as e:
            print(f"Warning: Could not create desktop shortcut: {e}")

class PostDevelopCommand(develop):
    """ডেভেলপমেন্ট মোড ইন্সটলেশনের পরে এক্সট্রা সেটআপ"""
    def run(self):
        develop.run(self)
        print("Development mode installation completed!")
        print("You can now run the IDE with: python src/main.py")

def read_requirements():
    """requirements.txt ফাইল থেকে ডিপেন্ডেন্সি পড়া"""
    try:
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return requirements
    except FileNotFoundError:
        return INSTALL_REQUIRES

def get_version():
    """ভার্সন নম্বর পড়া"""
    try:
        with open('VERSION', 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        return PROJECT_VERSION

def main():
    """মেইন সেটআপ ফাংশন"""
    
    # requirements.txt থেকে ডিপেন্ডেন্সি পড়া
    requirements = read_requirements()
    
    setup(
        name=PROJECT_NAME,
        version=get_version(),
        description=PROJECT_DESCRIPTION,
        long_description=PROJECT_LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author=PROJECT_AUTHOR,
        author_email=PROJECT_AUTHOR_EMAIL,
        url=PROJECT_URL,
        license=PROJECT_LICENSE,
        keywords=PROJECT_KEYWORDS,
        classifiers=CLASSIFIERS,
        
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        include_package_data=True,
        
        install_requires=requirements,
        extras_require=EXTRAS_REQUIRE,
        python_requires=">=3.8",
        
        entry_points=ENTRY_POINTS,
        
        cmdclass={
            'install': PostInstallCommand,
            'develop': PostDevelopCommand,
        },
        
        # প্যাকেজ ডেটা
        package_data={
            'appgenstudio': [
                'resources/icons/*',
                'resources/templates/*',
                'resources/syntax_themes/*',
                'config/*.json',
                'docs/*.md',
            ],
        },
        
        # ডেটা ফাইল
        data_files=[
            ('share/appgenstudio/resources', [
                'resources/icons/new_file.png',
                'resources/icons/save_file.png',
                'resources/icons/run_code.png',
            ]),
            ('share/appgenstudio/config', [
                'config/settings.json',
                'config/key_bindings.json',
            ]),
            ('share/appgenstudio/docs', [
                'docs/README.md',
                'docs/index.md',
            ]),
        ],
        
        # স্ক্রিপ্টস
        scripts=[
            'scripts/install_dependencies.sh',
            'scripts/build.py',
            'scripts/package.py',
        ],
    )

if __name__ == "__main__":
    main()