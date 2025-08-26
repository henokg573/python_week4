# 📂 File Read & Write Challenge (Python)

## 🖋️ Description
This program demonstrates **file handling** and **error management** in Python.  
It reads the content of a user-provided file, applies a simple modification (converts all text to **uppercase**), and writes the modified content to a **new file**.  

The program also handles common errors gracefully, such as when the file does not exist or cannot be opened.

---

## 🧪 Features
- Read file content from a user-specified filename.
- Modify the content (convert to uppercase).
- Save results into a new file (`modified_<filename>`).
- Error handling:
  - `FileNotFoundError` → if the file doesn’t exist
  - `PermissionError` → if the file can’t be read
  - General `Exception` → unexpected issues

---

## 🚀 How to Run
1. Clone or download this repository.
2. Open the terminal/command prompt in the project directory.
3. Run the program using:

   ```bash
   python file_handling.py
