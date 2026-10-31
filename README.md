# ticket-sla-breach-predictor

Predict which open tickets will breach their SLA: BREACHED, AT RISK (under 25% of SLA time left), or OK.

## How to run

```sh
python3 main.py tickets.csv --now 2026-10-29T12:00:00
```

## Example output

```
T-101: BREACHED
T-102: AT RISK
1 ticket(s) breached.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
