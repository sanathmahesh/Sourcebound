// Ask a follow-up: POST /api/ask. The answer uses the memo's chips and verdict labels; below it sit what the
// model looked up and the claims removed because they could not be verified. Busy, unavailable and
// out-of-scope outcomes are stated in words, never left to colour.
import { useState } from "react";
import type { AskResponse } from "../contracts/types";
import { formatDate, toFixedPy } from "../format";
import type { OpenSource } from "../sources";
import { ClaimText } from "./ClaimText";

const MAX = 500;

type Notice = { tone: "warn" | "bad" | "muted"; title: string; body: string };

type State =
  | { kind: "idle" }
  | { kind: "thinking" }
  | { kind: "notice"; notice: Notice }
  | { kind: "answer"; answer: AskResponse };

const RATE_LIMITED: Notice = { tone: "warn", title: "! Rate limited.", body: "Too many questions in a short time. Try again in a few minutes." };
const UNAVAILABLE: Notice = { tone: "bad", title: "✕ Model provider unavailable.", body: "The question was not answered. Nothing was changed. Try again later." };
const OUT_OF_SCOPE: Notice = { tone: "muted", title: "○ Out of scope.", body: "This tool answers questions about this company’s filings and credit profile only." };

function noticeFor(status: number, detail: string): Notice {
  if (status === 429) return RATE_LIMITED;
  if (status === 503) return UNAVAILABLE;
  return { tone: "bad", title: "✕ Not answered.", body: detail || `The request failed (HTTP ${status}).` };
}

export function AskPanel({ ticker, onOpen }: { ticker: string; onOpen: OpenSource }) {
  const [question, setQuestion] = useState("");
  const [state, setState] = useState<State>({ kind: "idle" });
  const busy = state.kind === "thinking";

  async function ask() {
    if (!question.trim() || busy) return;
    setState({ kind: "thinking" });
    try {
      const response = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticker, question: question.trim() }),
      });
      const body = await response.json().catch(() => ({}));
      if (!response.ok) {
        setState({ kind: "notice", notice: noticeFor(response.status, typeof body?.detail === "string" ? body.detail : "") });
        return;
      }
      const answer = body as AskResponse;
      setState(answer.status === "out_of_scope" ? { kind: "notice", notice: OUT_OF_SCOPE } : { kind: "answer", answer });
    } catch {
      setState({ kind: "notice", notice: { tone: "bad", title: "✕ Could not reach the server.", body: "Check your connection and try again." } });
    }
  }

  return (
    <section className="block" aria-label="Ask a follow-up">
      <h2 className="serif-h2">Ask a follow-up</h2>
      <p className="muted small-14 lede">Answers are drawn from the same filings and pass the same checks as the memo.</p>
      <form className="ask-form" onSubmit={(e) => { e.preventDefault(); ask(); }}>
        <input value={question} maxLength={MAX} aria-label="Question" placeholder="When does the revolver expire?"
          onChange={(e) => setQuestion(e.target.value)} />
        <button type="submit" disabled={busy || !question.trim()}>Ask</button>
      </form>
      {state.kind === "thinking" && (
        <div role="status" className="thinking">
          <span className="dots" aria-hidden="true"><span /><span /><span /></span> Searching filings and checking each claim…
        </div>
      )}
      {state.kind === "notice" && (
        <div role="alert" className={`notice notice-${state.notice.tone}`}>
          <strong>{state.notice.title}</strong> {state.notice.body}
        </div>
      )}
      {state.kind === "answer" && <Answer answer={state.answer} onOpen={onOpen} />}
    </section>
  );
}

function Answer({ answer, onOpen }: { answer: AskResponse; onOpen: OpenSource }) {
  const [traceOpen, setTraceOpen] = useState(false);
  return (
    <div className="answer">
      <div className="muted small">Q. {answer.question}</div>
      {answer.claims.length === 0 ? (
        <p className="muted">No claim in the answer could be verified, so nothing is shown. See the removed list below.</p>
      ) : (
        <p className="prose answer-prose">
          {answer.claims.map((claim) => (
            <span key={claim.id}>
              <ClaimText claim={claim} metrics={answer.metrics} passages={answer.passages} judgeModel={answer.judge_model} onOpen={onOpen} />{" "}
            </span>
          ))}
        </p>
      )}
      <div className="mono small muted">
        {answer.model} · checked by {answer.judge_model} · {toFixedPy(answer.seconds, 1)}s · data to {formatDate(answer.data_to)}
      </div>
      <div className="trace">
        <button type="button" className="trace-toggle" aria-expanded={traceOpen} onClick={() => setTraceOpen(!traceOpen)}>
          {traceOpen ? "▾" : "▸"} What was looked up ({answer.trace.length})
        </button>
        {traceOpen && (
          <ol className="trace-list">
            {answer.trace.map((t, n) => (
              <li key={n}>{t.tool}({JSON.stringify(t.arguments)}) <span className="muted">→ {t.result}</span></li>
            ))}
          </ol>
        )}
      </div>
      <div className="removed">
        <div className="strong small-14">Removed: could not be verified ({answer.removed.length})</div>
        {answer.removed.map((r, n) => (
          <div key={n} className="removed-item"><s className="muted">{r.text}</s> <span className="bad small">✕ {r.reason}</span></div>
        ))}
      </div>
    </div>
  );
}
