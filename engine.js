// Dryer Math engine - hypothetical arithmetic on labeled norms only.
// Duct, elbow and claim figures are illustrative norms; lint, sagging flex
// and crushed duct change real airflow.

function plural(n, one, many) { return n === 1 ? one : many; }

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function checkRun(feet, maxRun) {
  if (!(feet >= 0)) throw new Error("the straight duct must be zero or more");
  if (!(maxRun > 0)) throw new Error("the claimed run must be above zero");
}

function checkElbows(n90, n45) {
  if (!(n90 >= 0)) throw new Error("the 90-degree elbows must be zero or more");
  if (!(n45 >= 0)) throw new Error("the 45-degree elbows must be zero or more");
}

function runTruth(feet, n90, n45, maxRun) {
  checkRun(feet, maxRun);
  checkElbows(n90, n45);
  const eff = feet + 5 * n90 + 2.5 * n45;
  let verdict;
  if (eff <= maxRun * 0.5) verdict = "well inside the claim honestly";
  else if (eff <= maxRun) verdict = "inside the claim honestly";
  else verdict = `${fixed1(eff - maxRun)} feet past the claim honestly`;
  return `${feet} straight ${plural(feet, "foot", "feet")} with ${n90} 90-degree ${plural(n90, "elbow", "elbows")} and ${n45} 45-degree ${plural(n45, "elbow", "elbows")} counts as ${fixed1(eff)} feet - ${verdict}.`;
}

function elbowTruth(feet, maxRun) {
  checkRun(feet, maxRun);
  const left = maxRun - feet;
  if (left < 0) return `${feet} straight ${plural(feet, "foot", "feet")} is already ${fixed1(-left)} feet past the ${maxRun}-foot claim, before any elbows honestly.`;
  const elbows = Math.floor(left / 5 + 1e-9);
  let verdict;
  if (elbows === 0) verdict = "no elbows to spare honestly";
  else if (elbows <= 2) verdict = "a couple of elbows honestly";
  else if (elbows <= 5) verdict = "a few elbows honestly";
  else verdict = "elbows to spare honestly";
  return `After ${feet} straight ${plural(feet, "foot", "feet")}, the ${maxRun}-foot claim leaves room for ${elbows} 90-degree ${plural(elbows, "elbow", "elbows")} - ${verdict}.`;
}

function straightTruth(n90, n45, maxRun) {
  checkElbows(n90, n45);
  if (!(maxRun > 0)) throw new Error("the claimed run must be above zero");
  const used = 5 * n90 + 2.5 * n45;
  const left = maxRun - used;
  let tail;
  if (left < 0) tail = "the whole claim and then some honestly";
  else if (left === 0) tail = "the whole claim exactly honestly";
  else {
    let verdict;
    if (left >= maxRun * 0.7) verdict = "most of the run honestly";
    else if (left >= maxRun * 0.3) verdict = "about half the run honestly";
    else verdict = "a short stub honestly";
    tail = `leaving ${fixed1(left)} straight feet - ${verdict}`;
  }
  const verb = n90 + n45 === 1 ? "spends" : "spend";
  return `${n90} 90-degree and ${n45} 45-degree ${plural(n90 + n45, "elbow", "elbows")} ${verb} ${fixed1(used)} feet of the ${maxRun}-foot claim, ${tail}.`;
}

if (typeof module !== "undefined") {
  module.exports = { runTruth, elbowTruth, straightTruth };
}
