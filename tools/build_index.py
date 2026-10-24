"""build_index.py: rebuild index.json from animations/<Category>/<Name>.lua (run by the GitHub Action on every push; the hub reads index.json)."""
import json, os, re

REPO = os.environ.get("GITHUB_REPOSITORY", "HyperionElite/HyperionAnimations")


def stats(src):
    times = re.findall(r"Time\s*=\s*(-?[\d.]+(?:[eE][+-]?\d+)?)", src)
    try:
        dur = max(float(t) for t in times) if times else 0.0
    except ValueError:
        dur = 0.0
    return len(times), round(dur, 2)


def build_index(root):
    items, cats = [], {}
    base = os.path.join(root, "animations")
    for cat in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        cdir = os.path.join(base, cat)
        if not os.path.isdir(cdir):
            continue
        for fn in sorted(os.listdir(cdir), key=str.lower):
            if not fn.endswith(".lua"):
                continue
            p = os.path.join(cdir, fn)
            data = open(p, encoding="utf-8", errors="replace", newline="").read()
            kf, dur = stats(data)
            items.append({"n": fn[:-4], "c": cat, "f": cat + "/" + fn, "s": os.path.getsize(p), "k": kf, "d": dur})
            cats[cat] = cats.get(cat, 0) + 1
    index = {"v": 1, "repo": REPO, "branch": "main", "base": "animations/", "count": len(items), "categories": cats, "items": items}
    with open(os.path.join(root, "index.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(index, f, separators=(",", ":"), ensure_ascii=True)
    return index


if __name__ == "__main__":
    idx = build_index(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print("index.json:", idx["count"], "animations")
