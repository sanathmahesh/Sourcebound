// Ask a follow-up: POST /api/ask. The answer uses the memo's chips, citations and verdicts; below it sit
// what the model looked up and the claims removed because they could not be verified.
import { useState } from "react";
import type { AskResponse } from "../contracts/types";
import type { OpenSource } from "../sources";
import { ClaimText } from "./ClaimText";

const MAX = 500;

type State =
  | { kind: "idle" }
  | { kind: "thinking" }
  | { kind: "error"; message: string }
  | { kind: "answer"; answer: AskResponse };

const FALLBACK_MESSAGE: Record<number, string> = {
  429: "The service is busy. Try again in a few minutes.",
  503: "The model service is unavailable right now. Try again later.",
};

export function AskPanel({ ticker, onOpen }: { ticker: string; onOpen: OpenSource }) {
  const [question, setQuestion] = useState("");
  const [state, setState] = useState<State>({ kind: "idle" });

  async function ask() {
    setState({ kind: "thinking" });
    try {
      const response = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticker, question: question.trim() }),
      });
      const body = await response.json().catch(() => ({}));
      if (!response.ok) {
        const detail = typeof body?.detail === "string" ? body.detail : "";
        setState({ kind: "error", message: detail || FALLBACK_MESSAGE[response.status] || `Request failed (HTTP ${response.status}).` });
        return;
      }
      setState({ kind: "answer", answer: body as AskResponse });
    } catch {
      setState({ kind: "error", message: "Could not reach the server. Check your connection and try again." });
    }
  }

  return (
    <section className="ask" aria-label="Ask a follow-up">
      <h2>Ask a follow-up</h2>
      <form onSubmit={(e) => { e.preventDefault(); ask(); }}>
        <textarea value={question} maxLength={MAX} rows={3} placeholder="For example: how much of the revolver is drawn?"
          onChange={(e) => setQuestion(e.target.value)} />
        <div className="ask-row">
          <span className="note">{question.length} / {MAX}</span>
          <button type="submit" disabled={!question.trim() || state.kind === "thinking"}>Ask</button>
        </div>
      </form>
      {state.kind === "thinking" && <p role="status">Looking things up and checking each claim (up to a minute)…</p>}
      {state.kind === "error" && <p role="alert" className="error">{state.message}</p>}
      {state.kind === "answer" && <Answer answer={state.answer} onOpen={onOpen} />}
    </section>
  );
}

function Answer({ answer, onOpen }: { answer: AskResponse; onOpen: OpenSource }) {
  return (
    <div className="answer">
      {answer.status === "out_of_scope" ? (
        <p>That question is outside what this tool answers: it covers this company's credit, debt, liquidity,
          results, filings and SB scorecard.</p>
      ) : answer.claims.length === 0 ? (
        <p>No claim in the answer could be verified, so nothing is shown. See the removed list below.</p>
      ) : (
        <ul>
          {answer.claims.map((claim) => (
            <li key={claim.id}><ClaimText claim={claim} metrics={answer.metrics} passages={answer.passages} onOpen={onOpen} /></li>
          ))}
        </ul>
      )}
      <details>
        <summary>What was looked up ({answer.trace.length})</summary>
        <ol>
          {answer.trace.map((t, n) => (
            <li key={n}>Round {t.round}: <code>{t.tool}({JSON.stringify(t.arguments)})</code> → {t.result}</li>
          ))}
        </ol>
      </details>
      <details>
        <summary>Removed: could not be verified ({answer.removed.length})</summary>
        <ul>
          {answer.removed.map((r, n) => <li key={n}>{r.text} <span className="note">({r.reason})</span></li>)}
        </ul>
      </details>
      <p className="note">Answered by {answer.model}, checked by {answer.judge_model}, in {answer.seconds.toFixed(1)} s.
        Data to {answer.data_to ?? "not available"}.</p>
    </div>
  );
}
