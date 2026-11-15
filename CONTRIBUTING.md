# Contributing

## Branch and review policy

- Keep `main` as the shared stable branch. Do not commit or push project changes directly to it.
- Create a short-lived branch from an up-to-date `main`, for example `feat/image-upload` or `fix/image-validation`.
- Make focused commits on your branch and push that branch to GitHub.
- Open a pull request targeting `main`. Describe the change, how it was checked, and any known limitations.
- Ask a different team member to review the pull request. Authors should not approve their own changes.
- Merge only after the review and required checks pass.

Repository administrators should enable branch protection (or a ruleset) for `main` on GitHub: require pull requests, require at least one approval from someone other than the author, require the test workflow to pass, and block force pushes/deletion. The text in this file describes team practice; GitHub settings are needed to enforce it.

## Local development

1. Create and activate a virtual environment as described in the README.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Run checks with `python -m pytest` before opening a pull request.
4. Keep secrets in environment variables or a local ignored `.env` file. Never commit credentials, private data, or model weights without checking their size and license.
