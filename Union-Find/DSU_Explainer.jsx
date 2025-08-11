import React, { useMemo, useRef, useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Play, StepForward, RotateCcw } from "lucide-react";

// --- Minimal DSU implementation ---
class DSU {
  constructor(n) {
    this.n = n;
    this.p = Array.from({ length: n + 1 }, (_, i) => i);
    this.sz = Array(n + 1).fill(1);
  }
  find(x) {
    if (this.p[x] === x) return x;
    this.p[x] = this.find(this.p[x]);
    return this.p[x];
  }
  unite(a, b) {
    a = this.find(a);
    b = this.find(b);
    if (a === b) return false;
    if (this.sz[a] < this.sz[b]) [a, b] = [b, a];
    this.p[b] = a;
    this.sz[a] += this.sz[b];
    return true;
  }
  groups() {
    const mp = new Map();
    for (let i = 1; i <= this.n; i++) {
      const r = this.find(i);
      if (!mp.has(r)) mp.set(r, []);
      mp.get(r).push(i);
    }
    return Array.from(mp.values()).sort((A, B) => A[0] - B[0]);
  }
}

// Pretty badge for a person node
function Person({ id, highlight, truthy }) {
  return (
    <motion.div
      layout
      initial={{ scale: 0.9, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      exit={{ scale: 0.9, opacity: 0 }}
      className={`px-3 py-1 rounded-full text-sm font-medium shadow-sm border select-none
        ${highlight ? "bg-yellow-100 border-yellow-300" : "bg-white border-slate-200"}
        ${truthy ? "ring-2 ring-pink-400" : ""}`}
      title={truthy ? "진실 보유자 루트에 연결됨" : ""}
    >
      {id}
    </motion.div>
  );
}

function Chip({ children, tone = "slate" }) {
  const tones = {
    slate: "bg-slate-100 text-slate-800",
    green: "bg-green-100 text-green-800",
    red: "bg-rose-100 text-rose-800",
    amber: "bg-amber-100 text-amber-800",
    indigo: "bg-indigo-100 text-indigo-800",
  };
  return (
    <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${tones[tone]}`}>{children}</span>
  );
}

export default function DSUExplainer() {
  // --- Inputs (editable) ---
  const [n, setN] = useState(5);
  const [truthStr, setTruthStr] = useState("3");
  const [partyStr, setPartyStr] = useState(
    [
      "2 1 3",
      "2 2 3",
      "2 3 4",
      "2 5 3",
    ].join("\n")
  );

  // Parse inputs
  const truth = useMemo(() => truthStr.trim().split(/\s+/).filter(Boolean).map(Number), [truthStr]);
  const parties = useMemo(() => {
    // Each line: c p1 p2 ... pc
    return partyStr
      .split(/\n+/)
      .map((ln) => ln.trim())
      .filter(Boolean)
      .map((ln) => ln.split(/\s+/).map(Number))
      .map((arr) => (arr.length > 1 ? arr.slice(1) : []));
  }, [partyStr]);

  // Build union steps: for each party, union v[0] with v[j]
  const steps = useMemo(() => {
    const seq = [];
    parties.forEach((v, idx) => {
      if (v.length >= 2) {
        for (let j = 1; j < v.length; j++) {
          seq.push({ type: "union", a: v[0], b: v[j], partyIndex: idx });
        }
      }
    });
    seq.push({ type: "truthMark" });
    seq.push({ type: "evaluate" });
    return seq;
  }, [parties]);

  // Animation state
  const [stepIndex, setStepIndex] = useState(0);
  const [dsu, setDsu] = useState(() => new DSU(n));
  const [highlight, setHighlight] = useState({ a: null, b: null, partyIndex: null });
  const [truthRoots, setTruthRoots] = useState(new Set());
  const [partyStatus, setPartyStatus] = useState([]); // true => 거짓 가능, false => 불가
  const [playing, setPlaying] = useState(false);

  // Reset when inputs change
  useEffect(() => {
    setDsu(new DSU(n));
    setStepIndex(0);
    setHighlight({ a: null, b: null, partyIndex: null });
    setTruthRoots(new Set());
    setPartyStatus([]);
    setPlaying(false);
  }, [n, truthStr, partyStr]);

  // Play loop
  useEffect(() => {
    if (!playing) return;
    if (stepIndex >= steps.length) {
      setPlaying(false);
      return;
    }
    const t = setTimeout(() => doStep(), 900);
    return () => clearTimeout(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [playing, stepIndex, steps]);

  const doStep = () => {
    if (stepIndex >= steps.length) return;
    const s = steps[stepIndex];
    if (s.type === "union") {
      const next = new DSU(dsu.n);
      next.p = dsu.p.slice();
      next.sz = dsu.sz.slice();
      next.unite(s.a, s.b);
      setDsu(next);
      setHighlight({ a: s.a, b: s.b, partyIndex: s.partyIndex });
      setStepIndex((i) => i + 1);
      return;
    }
    if (s.type === "truthMark") {
      const roots = new Set(truth.map((t) => dsu.find(t)));
      setTruthRoots(roots);
      setHighlight({ a: null, b: null, partyIndex: null });
      setStepIndex((i) => i + 1);
      return;
    }
    if (s.type === "evaluate") {
      const roots = new Set(truth.map((t) => dsu.find(t)));
      const status = parties.map((v) => {
        // 거짓 가능: 참석자 중 진실 루트가 없으면 true
        const hasTruth = v.some((x) => roots.has(dsu.find(x)));
        return !hasTruth;
      });
      setPartyStatus(status);
      setStepIndex((i) => i + 1);
      return;
    }
  };

  const onPlay = () => {
    if (stepIndex >= steps.length) return;
    setPlaying(true);
  };
  const onStep = () => {
    setPlaying(false);
    doStep();
  };
  const onReset = () => {
    setPlaying(false);
    setDsu(new DSU(n));
    setStepIndex(0);
    setHighlight({ a: null, b: null, partyIndex: null });
    setTruthRoots(new Set());
    setPartyStatus([]);
  };

  // Computed visuals
  const groups = useMemo(() => dsu.groups(), [dsu]);
  const result = useMemo(() => partyStatus.filter(Boolean).length, [partyStatus]);

  return (
    <div className="w-full min-h-screen bg-slate-50 text-slate-800 p-6">
      <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Controls */}
        <div className="md:col-span-1 space-y-4">
          <h1 className="text-2xl font-bold">DSU로 보는 “거짓말” 애니메이션</h1>
          <p className="text-sm leading-relaxed">
            파티별로 참석자들을 <b>union</b> 해서 사람 그래프의 연결 컴포넌트를 만들고,
            <br />
            진실 보유자와 같은 <b>루트</b>에 속한 파티는 <b>거짓말 불가</b>로 표시합니다.
          </p>

          <div className="space-y-3 bg-white rounded-2xl shadow p-4 border border-slate-200">
            <label className="block text-sm font-medium">사람 수 N</label>
            <input
              type="number"
              min={1}
              max={50}
              value={n}
              onChange={(e) => setN(parseInt(e.target.value || "1", 10))}
              className="w-full rounded-lg border px-3 py-2"
            />
            <label className="block text-sm font-medium">진실 보유자 (공백 구분)</label>
            <input
              value={truthStr}
              onChange={(e) => setTruthStr(e.target.value)}
              className="w-full rounded-lg border px-3 py-2"
              placeholder="예: 2 5"
            />
            <label className="block text-sm font-medium">파티 목록 (한 줄: 인원수 p1 p2 ...)</label>
            <textarea
              rows={6}
              value={partyStr}
              onChange={(e) => setPartyStr(e.target.value)}
              className="w-full rounded-lg border px-3 py-2 font-mono text-sm"
            />

            <div className="flex items-center gap-2 pt-2">
              <button onClick={onPlay} disabled={playing || stepIndex >= steps.length}
                className="inline-flex items-center gap-2 px-3 py-2 rounded-xl shadow-sm bg-indigo-600 text-white disabled:opacity-50">
                <Play size={16}/> Play
              </button>
              <button onClick={onStep} disabled={stepIndex >= steps.length}
                className="inline-flex items-center gap-2 px-3 py-2 rounded-xl shadow-sm bg-slate-800 text-white disabled:opacity-50">
                <StepForward size={16}/> Step
              </button>
              <button onClick={onReset}
                className="inline-flex items-center gap-2 px-3 py-2 rounded-xl shadow-sm bg-white border">
                <RotateCcw size={16}/> Reset
              </button>
            </div>

            <div className="text-xs text-slate-600 pt-1">
              현재 단계: {stepIndex}/{steps.length}
            </div>
          </div>

          <div className="bg-white rounded-2xl shadow p-4 border border-slate-200 space-y-2">
            <h2 className="font-semibold">설명 스크립트</h2>
            <ol className="list-decimal list-inside text-sm space-y-1">
              <li>각 파티의 참석자들을 <b>DSU union</b>으로 묶습니다.</li>
              <li>진실을 아는 사람들의 <b>루트(대표자)</b>를 표시합니다.</li>
              <li>각 파티에 진실 루트에 속한 사람이 있으면 <Chip tone="red">거짓 불가</Chip>, 아니면 <Chip tone="green">거짓 가능</Chip>.</li>
            </ol>
          </div>
        </div>

        {/* Visualization */}
        <div className="md:col-span-2 space-y-4">
          <div className="bg-white rounded-2xl shadow p-4 border border-slate-200">
            <div className="flex items-center justify-between mb-2">
              <h2 className="font-semibold">사람 그룹(DSU 컴포넌트)</h2>
              <div className="text-sm">진실 루트: <Chip tone="amber">핑크 링</Chip> 표시</div>
            </div>

            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">
              <AnimatePresence>
                {groups.map((grp, idx) => {
                  const root = grp.length ? dsu.find(grp[0]) : -1;
                  const truthy = truthRoots.has(root);
                  return (
                    <motion.div key={"grp-" + idx}
                      layout
                      className={`p-3 rounded-2xl border ${truthy ? "border-pink-400 bg-pink-50" : "border-slate-200 bg-slate-50"}`}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <div className="font-medium">Root {root}</div>
                        {truthy ? <Chip tone="amber">truth</Chip> : <Chip>group</Chip>}
                      </div>
                      <div className="flex flex-wrap gap-2">
                        {grp.map((id) => (
                          <Person
                            key={id}
                            id={id}
                            truthy={truthy}
                            highlight={highlight.a === id || highlight.b === id}
                          />
                        ))}
                      </div>
                    </motion.div>
                  );
                })}
              </AnimatePresence>
            </div>
          </div>

          <div className="bg-white rounded-2xl shadow p-4 border border-slate-200">
            <div className="flex items-center justify-between mb-2">
              <h2 className="font-semibold">파티 목록</h2>
              <div className="text-sm">현재 union 대상은 <Chip tone="indigo">노란 하이라이트</Chip></div>
            </div>

            <div className="grid sm:grid-cols-2 gap-3">
              {parties.map((v, idx) => {
                const status = partyStatus[idx];
                return (
                  <div key={idx} className={`p-3 rounded-2xl border ${status === undefined ? "border-slate-200 bg-slate-50" : status ? "border-green-300 bg-green-50" : "border-rose-300 bg-rose-50"}`}>
                    <div className="flex items-center justify-between mb-2">
                      <div className="font-medium">Party {idx + 1}</div>
                      {status === undefined ? <Chip>pending</Chip> : status ? <Chip tone="green">거짓 가능</Chip> : <Chip tone="red">거짓 불가</Chip>}
                    </div>
                    <div className="flex flex-wrap gap-2">
                      {v.map((id, j) => (
                        <Person
                          key={j + "-" + id}
                          id={id}
                          truthy={truthRoots.has(dsu.find(id))}
                          highlight={highlight.partyIndex === idx && (highlight.a === id || highlight.b === id)}
                        />
                      ))}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          <div className="bg-white rounded-2xl shadow p-4 border border-slate-200 flex items-center justify-between">
            <div className="text-lg font-semibold">거짓말 가능 파티 수</div>
            <div className="text-3xl font-black">{result}</div>
          </div>
        </div>
      </div>
    </div>
  );
}