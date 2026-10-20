#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import json
from pathlib import Path

data = json.loads(Path('feature_list.json').read_text())
features = data['features']
valid = set(data['rules']['valid_status'])
active = [f for f in features if f['status'] == 'in_progress']
if len(active) > 1:
    raise SystemExit('ERROR: solo puede existir una feature in_progress')

for feature in features:
    if feature['status'] not in valid:
        raise SystemExit(f"ERROR: estado inválido en {feature['name']}: {feature['status']}")
    if not feature.get('name') or not feature.get('description') or not feature.get('acceptance'):
        raise SystemExit(f"ERROR: feature incompleta: {feature.get('name', '<sin nombre>')}")

for feature in features:
    if feature.get('sdd'):
        spec = Path('specs') / feature['name']
        if feature['status'] in {'spec_ready', 'in_progress', 'done'}:
            required = [spec/'requirements.md', spec/'design.md', spec/'tasks.md']
            missing = [str(p) for p in required if not p.exists()]
            if missing:
                raise SystemExit('ERROR: faltan specs: ' + ', '.join(missing))
            requirements = (spec / 'requirements.md').read_text()
            if '## R1' not in requirements:
                raise SystemExit(f"ERROR: {spec/'requirements.md'} no contiene requirements R<n>")
            tasks = (spec / 'tasks.md').read_text()
            if 'T1' not in tasks:
                raise SystemExit(f"ERROR: {spec/'tasks.md'} no contiene tasks T<n>")
print('[OK] Harness estructural listo')
PY

for required in AGENTS.md feature_list.json progress/current.md docs/architecture.md docs/specs.md CHECKPOINTS.md; do
  if [ ! -f "$required" ]; then
    echo "ERROR: falta archivo base: $required"
    exit 1
  fi
done

if [ -d tests ]; then
  if find tests -type f -name 'test_*.py' | grep -q .; then
    python3 -m pytest -q
  else
    echo "[WARN] tests/ existe pero aún no contiene pruebas"
  fi
else
  echo "[WARN] tests/ aún no existe; se creará durante la implementación"
fi

echo "[OK] Entorno Harness listo"
