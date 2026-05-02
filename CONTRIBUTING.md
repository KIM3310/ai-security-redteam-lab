# Contributing

Run the local checks before changing detectors or fixtures:

```bash
python3 -m unittest discover -s tests
python3 scripts/run_scan.py
```

New detector rules should include one positive case and one benign case.
