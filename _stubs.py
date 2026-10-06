"""RuleArena's reference modules import API clients at top level that the reference compute never calls."""
import sys, types
for _m in ("openai", "anthropic", "vertexai", "google", "google.auth", "google.auth.transport"):
    sys.modules.setdefault(_m, types.ModuleType(_m))
