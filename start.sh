#!/usr/bin/env zsh

# startvirtualpythonenv.sh (zsh)
# Activate a Python virtual environment in the CURRENT zsh session.
#
# Usage (must be sourced):
#   source ./startvirtualpythonenv.sh
#   . ./startvirtualpythonenv.sh

# If executed instead of sourced, tell the user what to do.
if [[ "${ZSH_EVAL_CONTEXT:-}" != *:file ]]; then
  print -u2 "This script must be sourced to activate the virtual environment in your current shell:"
  print -u2 "  source ./startvirtualpythonenv.sh"
  print -u2 "  . ./startvirtualpythonenv.sh"
  exit 1
fi

# Resolve this script's directory (works when sourced)
SCRIPT_DIR="${0:A:h}"``
cd "$SCRIPT_DIR" || return 1

# Prefer an existing .venv if you already have one.
# Common names are: .venv/ or ..venv/
VENV_DIR=""

if [[ -f "$SCRIPT_DIR/venv/bin/activate" ]]; then
  VENV_DIR="$SCRIPT_DIR/venv"
elif [[ -f "$SCRIPT_DIR/.venv/bin/activate" ]]; then
  VENV_DIR="$SCRIPT_DIR/.venv"
else
  VENV_DIR="$SCRIPT_DIR/venv"
  print "No existing venv found. Creating virtual environment at: $VENV_DIR"
  python3 -m .venv "$VENV_DIR" || return 1
fi

if [[ ! -f "$VENV_DIR/bin/activate" ]]; then
  print -u2 "Error: Expected activation script not found at: $VENV_DIR/bin/activate"
  return 1
fi

# Activate .venv in the CURRENT shell
source "$VENV_DIR/bin/activate"

# Optional: keep tooling fresh (quietly). Don't fail activation if it fails.
python -m pip install --upgrade pip >/dev/null 2>&1 || true

print "Activated virtual environment: $VENV_DIR"
print "Python: $(command -v python)"
