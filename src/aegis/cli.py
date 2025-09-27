import argparse
import json
from . import __version__

def main():
    parser = argparse.ArgumentParser(description="Aegis MVP (Commit 1): config echo CLI")
    parser.add_argument("--attack", choices=["phishing_malware", "web_attack", "ransomware"], default="web_attack")
    parser.add_argument("--duration", type=int, default=300, help="Simulation duration in seconds")
    parser.add_argument("--volume", choices=["low", "medium", "high"], default="medium")
    parser.add_argument(
        "--formats",
        nargs="+",
        default=["zeek", "okta", "nginx"],
        help="Output formats to target (e.g., zeek okta nginx)",
    )
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    config = {
        "attack": args.attack,
        "duration": args.duration,
        "volume": args.volume,
        "formats": args.formats,
        "seed": args.seed,
        "version": __version__,
        "status": "OK (commit 1 skeleton)",
    }
    print(json.dumps(config, indent=2))

