python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
reflex init
reflex run --env prod --loglevel debug
deactivate