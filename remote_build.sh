python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

reflex init
reflex run --env prod

deactivate