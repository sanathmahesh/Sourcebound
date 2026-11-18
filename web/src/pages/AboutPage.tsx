// Screen 6: About. The six strategy documents, method, model card and limitations arrive in phase 8 as
// /data/about.json; until then this page says what the project is and what is still to come.
export function AboutPage() {
  return (
    <article>
      <h1>About Sourcebound</h1>
      <p>Sourcebound drafts a credit memo on a US public company from its SEC filings and checks every figure and
        claim against source data. Figures are computed by code from the company's XBRL data and shown as
        placeholders the model cannot change; quoted figures must appear in the passage they cite; and an
        independent model judges whether each claim is supported. Anything unverified stays visible and goes on a
        checklist for a person to sign off.</p>
      <p>The strategy documents (opportunity map, manual versus tool-assisted effort, model recommendation, risk and
        control table, rollout plan, decision log), the method, the model card and the limitations will appear here
        in a later phase.</p>
      <p className="note">Educational project. Not investment advice. SB grades are a student's stylized scorecard,
        not credit ratings.</p>
    </article>
  );
}
