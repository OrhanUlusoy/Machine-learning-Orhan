# Project-specific bashrc for VS Code terminal
# Loads your normal bashrc (if any) and then auto-activates this project's venv.

if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi

# Resolve project root from this file location (works even if the terminal starts elsewhere)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Ensure venv activation can show in prompt
unset VIRTUAL_ENV_DISABLE_PROMPT

# If a venv was previously activated but the folder no longer exists, deactivate/unset it
if [ -n "${VIRTUAL_ENV:-}" ] && [ ! -d "$VIRTUAL_ENV" ]; then
  if type deactivate >/dev/null 2>&1; then
    deactivate
  fi
  unset VIRTUAL_ENV
fi

# Auto-activate project venv if present
if [ -f "$PROJECT_ROOT/.venv/Scripts/activate" ]; then
  . "$PROJECT_ROOT/.venv/Scripts/activate"
fi
