# Dryer Math

Honest dryer-vent arithmetic. The box claims a thirty-five-foot run; Dryer Math counts what
the elbows spend, what the claim has left, and what the route really adds up to.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The run truth** - straight feet plus elbows against the claimed maximum run.
- **The elbow truth** - after the straight feet, the 90-degree bends the claim can still afford.
- **The straight truth** - the elbows priced first: the straight feet the claim leaves behind.

## The boundary

Dryer Math keeps duct-length arithmetic only. Every foot and elbow figure is a labeled norm,
not a promise - lint, sagging flex and crushed duct change real airflow, and lint is a fire
hazard. Follow the dryer's manual and local code over anything this page says, and clean the
lint path on the schedule the manufacturer sets. Every figure is hypothetical arithmetic on
labeled norms, not a statement about any real dryer, duct or installation.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json
node test.js        # 26 cases / 26 checks, 0 failed
```
