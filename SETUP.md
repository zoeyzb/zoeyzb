# Profile maintenance

This repository combines two MIT-licensed profile tools:

- **Paper Signal** supplies the editorial cover and selected-work folio. Edit `config.json`, then run `python scripts/generate.py` to refresh `assets/cover.svg` and `assets/folio.svg`.
- **Readme Atelier** supplies the contribution activity and technology-stack cards. Edit `atelier.yml`; the pinned GitHub Action refreshes the generated block in `README.md`.

## Local preview

```bash
python scripts/generate.py --demo
GITHUB_TOKEN="$(gh auth token)" python scripts/generate.py
GITHUB_TOKEN="$(gh auth token)" node /path/to/readme-atelier/dist/cli.js build --user zoeyzb --config atelier.yml --out . --preview
```

The hosted workflow runs both generators in sequence and creates one commit, avoiding competing README writers. It uses GitHub's repository token and does not require a personal access token stored in repository secrets.

## What to edit

- `config.json`: display name, role, statement, services and the three projects shown in the folio.
- `atelier.yml`: theme, short bio, technology stack, social links and generated sections.
- `README.md`: project summaries, case-study links and contact information. Leave the `readme-atelier` markers in place.
- `case-studies/`: sanitized technical summaries of private projects. Never add `.env` files, customer data, private credentials, API keys or proprietary source code.

## Publishing notes

The profile README is public. The private case studies describe scope only; the original private repositories remain private. The project summaries explicitly distinguish illustrative demos and incomplete external validation from live, verified behavior.
