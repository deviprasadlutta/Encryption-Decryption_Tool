#  File Encryption & Decryption Tool (Python)

A simple and secure **command-line tool** to **encrypt** and **decrypt** text files using symmetric key cryptography with the `Fernet` module from the `cryptography` library.  
This tool is designed to teach beginners the basics of file security, using **symmetric encryption** to protect sensitive data.

---

## Features

- **Generate secure encryption keys**.
- **Encrypt any text file** (`.txt`).
- **Decrypt encrypted files** using the same key.
- **Save output files** (encrypted or decrypted) to custom paths.
- **Easy-to-use CLI tool with clear prompts.

---

## Requirements

- Python 3.x (tested on 3.8+)
- [`cryptography`](https://pypi.org/project/cryptography/) library

###  Install Required Package

To install the `cryptography` package, use the following pip command:

```bash
pip install cryptography
