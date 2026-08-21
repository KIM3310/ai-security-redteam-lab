# Contributing

Run the local checks before changing detectors or fixtures:

```bash
make verify
python3 scripts/run_scan.py
```

New detector rules should include one positive case and one benign case.
