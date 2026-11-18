# Labelling the claims (blind)

Open `labelling-sheet.csv` in a spreadsheet. Each row is one claim from a memo, with the passage(s) it cites
or the engine figures it states. The rows are shuffled and do not say which model wrote them. Do not open
`key.json` until you have finished.

For each row fill in:
- **my verdict**: `S` supported (everything in the claim is stated in, or follows directly from, the
  evidence), `P` partially supported (some of it is, some goes beyond or overstates), `U` unsupported (the
  evidence does not support it, or contradicts it). Judge only against the evidence shown.
- **citation correct**: `Y` if the cited passage is relevant to the claim and is where you would look for
  it, `N` if not; leave blank when the claim cites nothing.
- **notes**: anything odd, optional.

Save the file under the same name (CSV). Partial labelling is fine: the report counts what you have done
and states the sample size.
