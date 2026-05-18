#!/usr/bin/env python3
"""AETHORFORGE v1.9 — World Serpent"""
import sys, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

BANNER = """
╔══════════════════════════════════════╗
║   AETHORFORGE v1.9  World Serpent   ║
║   Cyber · Energy · Biotech          ║
║   Finance · Learning · Voice        ║
╚══════════════════════════════════════╝"""

MODES = {
    "1": "router",
    "2": "crucible",
    "3": "pentest",
    "4": "bounty",
    "5": "voice",
    "q": "quit"
}

def main():
    print(BANNER)
    key = os.environ.get("GROQ_API_KEY","")
    print(f"  Groq: {'✓ set' if key else '✗ not set — export GROQ_API_KEY=gsk_...'}\n")

    from code.dmaas.hybrid_router import HybridRouter
    from code.crucible.spartan_crucible import SpartanCrucible

    router   = HybridRouter()
    crucible = SpartanCrucible()

    print("\n✓ AETHORFORGE ONLINE — type query or q to quit\n")

    while True:
        try:
            query = input("⚡ > ").strip()
            if not query: continue
            if query.lower() == "q": break
            cx = input("  complexity 1-10 [Enter=auto]: ").strip()
            complexity = int(cx) if cx.isdigit() else None
            result = router.route(query, complexity)
            print(f"\n{result}\n{'─'*50}")
        except KeyboardInterrupt:
            break

    print("\n👋 World Serpent offline.\n")

if __name__ == "__main__":
    main()

