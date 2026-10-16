import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def check_run(feet, max_run):
    if not (feet >= 0):
        raise ValueError("the straight duct must be zero or more")
    if not (max_run > 0):
        raise ValueError("the claimed run must be above zero")

def check_elbows(n90, n45):
    if not (n90 >= 0):
        raise ValueError("the 90-degree elbows must be zero or more")
    if not (n45 >= 0):
        raise ValueError("the 45-degree elbows must be zero or more")

def run_truth(feet, n90, n45, max_run):
    check_run(feet, max_run)
    check_elbows(n90, n45)
    eff = feet + 5 * n90 + 2.5 * n45
    if eff <= max_run * 0.5:
        verdict = "well inside the claim honestly"
    elif eff <= max_run:
        verdict = "inside the claim honestly"
    else:
        verdict = f"{fixed1(eff - max_run)} feet past the claim honestly"
    return f"{feet} straight {plural(feet, 'foot', 'feet')} with {n90} 90-degree {plural(n90, 'elbow', 'elbows')} and {n45} 45-degree {plural(n45, 'elbow', 'elbows')} counts as {fixed1(eff)} feet - {verdict}."

def elbow_truth(feet, max_run):
    check_run(feet, max_run)
    left = max_run - feet
    if left < 0:
        return f"{feet} straight {plural(feet, 'foot', 'feet')} is already {fixed1(-left)} feet past the {max_run}-foot claim, before any elbows honestly."
    elbows = math.floor(left / 5 + 1e-9)
    if elbows == 0:
        verdict = "no elbows to spare honestly"
    elif elbows <= 2:
        verdict = "a couple of elbows honestly"
    elif elbows <= 5:
        verdict = "a few elbows honestly"
    else:
        verdict = "elbows to spare honestly"
    return f"After {feet} straight {plural(feet, 'foot', 'feet')}, the {max_run}-foot claim leaves room for {elbows} 90-degree {plural(elbows, 'elbow', 'elbows')} - {verdict}."

def straight_truth(n90, n45, max_run):
    check_elbows(n90, n45)
    if not (max_run > 0):
        raise ValueError("the claimed run must be above zero")
    used = 5 * n90 + 2.5 * n45
    left = max_run - used
    if left < 0:
        tail = "the whole claim and then some honestly"
    elif left == 0:
        tail = "the whole claim exactly honestly"
    else:
        if left >= max_run * 0.7:
            verdict = "most of the run honestly"
        elif left >= max_run * 0.3:
            verdict = "about half the run honestly"
        else:
            verdict = "a short stub honestly"
        tail = f"leaving {fixed1(left)} straight feet - {verdict}"
    verb = "spends" if n90 + n45 == 1 else "spend"
    return f"{n90} 90-degree and {n45} 45-degree {plural(n90 + n45, 'elbow', 'elbows')} {verb} {fixed1(used)} feet of the {max_run}-foot claim, {tail}."

FNS = {"runTruth": run_truth, "elbowTruth": elbow_truth, "straightTruth": straight_truth}

cases = [
 {"fn":"runTruth","args":[12,3,1,35]},
 {"fn":"runTruth","args":[5,0,0,35]},
 {"fn":"runTruth","args":[20,2,2,35]},
 {"fn":"runTruth","args":[25,3,0,35]},
 {"fn":"runTruth","args":[1,0,1,35]},
 {"fn":"runTruth","args":[0,1,0,35]},
 {"fn":"runTruth","args":[-1,0,0,35]},
 {"fn":"runTruth","args":[12,0,0,0]},
 {"fn":"runTruth","args":[12,-1,0,35]},
 {"fn":"elbowTruth","args":[12,35]},
 {"fn":"elbowTruth","args":[33,35]},
 {"fn":"elbowTruth","args":[25,35]},
 {"fn":"elbowTruth","args":[5,35]},
 {"fn":"elbowTruth","args":[40,35]},
 {"fn":"elbowTruth","args":[35,35]},
 {"fn":"elbowTruth","args":[0,35]},
 {"fn":"elbowTruth","args":[12,0]},
 {"fn":"straightTruth","args":[3,1,35]},
 {"fn":"straightTruth","args":[1,0,35]},
 {"fn":"straightTruth","args":[0,0,35]},
 {"fn":"straightTruth","args":[6,2,35]},
 {"fn":"straightTruth","args":[5,1,35]},
 {"fn":"straightTruth","args":[0,1,35]},
 {"fn":"straightTruth","args":[8,0,35]},
 {"fn":"straightTruth","args":[3,1,0]},
 {"fn":"straightTruth","args":[-1,0,35]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
