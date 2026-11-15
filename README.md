# PlantDoctor

PlantDoctor is a student project exploring an AI assistant that uses a photo of a plant to identify the plant, check for possible disease, and provide useful plant-care information.

## Project status

This repository currently contains the Python project scaffold, basic image and label validation utilities, and automated tests. **It does not yet contain a trained model, disease dataset, plant identification system, or a user-facing application.** It cannot diagnose a plant at this stage. The model and app directories are reserved for that future work.

## Requirements

- Python 3.10 or newer
- pip

## Installation

Clone the repository and enter its directory:

```bash
git clone https://github.com/alekpavlov-boop/PlantDoctor.git
cd PlantDoctor
```

Create and activate a virtual environment:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the current project checks

Run the test suite from the repository root:

```bash
python -m pytest
```

The tests cover label cleanup, image input validation, and the prediction interface using a small fake model. This checks the project plumbing; it does not measure disease-detection accuracy.

## Repository layout

```text
PlantDoctor/
├── app/                 # Future user interface
├── data/                # Dataset location; do not commit private or large raw data
├── src/plantdoctor/     # Reusable project code
├── tests/               # Automated tests
├── .github/             # Pull request template and CI workflow
├── CONTRIBUTING.md      # Branch and review workflow
└── requirements.txt
```

## Collaboration workflow

Work on a feature or fix branch and open a pull request to `main`. A different team member should review each pull request before it is merged. Do not push project changes directly to `main`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the steps. GitHub branch protection should also be enabled by a repository administrator to enforce these rules on GitHub.

## Limitations and responsible use

- There is no trained model or diagnosis feature yet.
- Future predictions will depend on the plants and conditions represented in the training data. Results may be wrong, especially for blurry photos, unusual lighting, mixed symptoms, or unsupported plants.
- A photo-based result should be presented as an estimate, not a guaranteed diagnosis or a substitute for advice from a qualified horticulture or agricultural specialist.
- Any future dataset must be used in line with its license and documented source. Avoid committing secrets, personal data, or large datasets; use an approved storage method for those.

## License

No license has been added yet. Until the project owners choose one, reuse and redistribution permissions are not specified.
