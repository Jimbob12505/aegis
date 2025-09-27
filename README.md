
# Aegis MVP — Synthetic Security Log Generator (Local)

Minimal, local-first prototype to generate synthetic logs for **Zeek**, **Okta**, and **NGINX**
from a simple scenario blueprint (e.g., `phishing_malware`, `web_attack`).

## Quick start

```bash
python -m aegis.cli --attack web_attack --duration 300 --volume medium --formats zeek okta nginx --out ./output
```

Outputs will be written under `./output/<run_id>/`:

- `zeek/conn.log`
- `okta/okta.json`
- `nginx/access_combined.log`
- `nginx/access.jsonl`
- `labels.json`

> This MVP is intentionally dependency-light (stdlib only). It uses a simple Markov model for benign web traffic and deterministic seeds for reproducibility.
```
