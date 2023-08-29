> ⚠️ OpenModdEditor is still in an early development stage. Numerous bugs and unfinished features are to be expected!
# OpenModdEditor
![Editor](assets/editor.jpg)
## Cross-platform modd.io game editor
OpenModdEditor is a cross-platform game editor to create 2D multiplayer .io games.
It uses Taro2 for the backend, which makes games made with it compatible with modd.io.
## License
OpenModdEditor is completely free and open source under the APGL License!
This license applies to the entire repo except for subfolders that have their own license file. In such cases, the license file in the subfolder takes precedence.
## Getting OpenModdEditor
### Binary Downloads:
There are no downloadable binaries yet, as the project is still very unstable!
### Build OpenModdEditor from source:
**Build Prerequisites:**
Ensure you have python, pip, git, rust, cargo, node.js & npm installed!
For Windows you also need the latest Microsoft Visual C++ Redistributable.

**Build steps:**

***Linux:***
```
git clone https://codeberg.org/Boorb/OpenModdEditor.git
```
```
cd OpenModdEditor
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```
```
pyinstaller index.spec
```
```
./dist/index/index 
```
***Windows:***
```
git clone https://codeberg.org/Boorb/OpenModdEditor.git
```
```
cd OpenModdEditor
```
```
python3 -m venv venv
```
```
venv\Scripts\activate
```
> If this command fails, try executing **Set-ExecutionPolicy Unrestricted -Scope Process** as root in a PowerShell window.
```
pip install -r requirements.txt
```
```
pyinstaller index.spec
```
```
./dist/index/index 
```