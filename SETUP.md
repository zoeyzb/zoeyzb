# Profile maintenance

The profile uses a small Paper Signal-inspired SVG identity system and a curated public case-study repository.

- `config.json` contains the display name, statement, services and featured projects.
- `scripts/generate.py` renders `assets/cover.svg` and `assets/folio.svg` from that configuration.
- `README.md` contains the project summaries and links to `https://github.com/zoeyzb/selected-work`.
- The `selected-work` repository contains sanitized case studies and screenshots for projects whose source code remains private.

## Refresh artwork

```bash
GITHUB_TOKEN="$(gh auth token)" python scripts/generate.py
```

The script checks that the selected public repositories exist, then regenerates the two SVG assets. GitHub's native contribution graph updates independently; no third-party activity heatmap is embedded.

Never add `.env` files, credentials, customer records, private source code or proprietary configuration to the public profile or case-study repository.
