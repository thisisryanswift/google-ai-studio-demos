# AI Studio Demo Steps

1. Grab an API Key and replace the value in `.env`
2. Set up your Python environment:

   **Option A: Using `uv` (Recommended)**
   ```bash
   uv sync
   ```

   **Option B: Using traditional `venv` and `pip`**

   Create and activate a virtual environment:
   ```bash
   python -m venv venv
   ```

   Then activate it:

   For Windows (PowerShell):
   ```powershell
   venv\Scripts\Activate.ps1
   ```

   For macOS/Linux (bash/zsh):
   ```bash
   source ./venv/bin/activate
   ```

   Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run any of the demo files:
   ```bash
   python 1_quickstart.py
   ```

4. Bounce between VS Code and AI Studio as you perform each demo.