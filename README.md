# Google AI Studio Demos
Just some quick helpers for MLHers running the Intro to Google AI Studio workshop.

1. Grab an API Key from mlh.link/aistudio and replace the value in `.env`
   - Also update your hackathon name and the url you'd like to use for url_context.
   - You can type these in manually if you prefer!
2. Set up your Python environment:

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