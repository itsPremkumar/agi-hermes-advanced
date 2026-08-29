#!/usr/bin/env python3
"""
belief_graph_manager.py — Persistent Belief & Mission Graph Manager
Provides deterministic SQLite-backed tracking of claims, evidence URLs,
confidence calibrations, contradictions, and dependent downstream beliefs.

Usage:
    python belief_graph_manager.py add --claim "Hermes uses 15 planes" --confidence 0.95 --source "https://hermes.nousresearch.com"
    python belief_graph_manager.py list
    python belief_graph_manager.py contradict --claim-id 1 --reason "Alternative spec found" --penalty 0.2
    python belief_graph_manager.py export --format markdown
"""

import os
import sys
import sqlite3
import pathlib
import argparse
from datetime import datetime

DEFAULT_DB_PATH = pathlib.Path.home() / ".hermes" / "belief_graph.db"

def get_connection(db_path: pathlib.Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS beliefs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            claim TEXT UNIQUE NOT NULL,
            confidence REAL NOT NULL,
            sources TEXT NOT NULL,
            contradictions INTEGER DEFAULT 0,
            dependent_beliefs TEXT DEFAULT '[]',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn

def add_belief(conn: sqlite3.Connection, claim: str, confidence: float, source: str):
    now = datetime.now().isoformat()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO beliefs (claim, confidence, sources, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(claim) DO UPDATE SET
            confidence = excluded.confidence,
            sources = sources || ',' || excluded.sources,
            updated_at = excluded.updated_at
    """, (claim, confidence, source, now, now))
    conn.commit()
    print(f"[BELIEF GRAPH] Saved claim (id={cursor.lastrowid}): '{claim}' (Confidence: {confidence:.2f})")

def list_beliefs(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("SELECT id, claim, confidence, contradictions, updated_at FROM beliefs ORDER BY confidence DESC")
    rows = cursor.fetchall()
    print("\n==================== HERMES ACTIVE BELIEF GRAPH ====================")
    print(f"{'ID':<4} | {'CONF':<6} | {'CONTR':<5} | {'CLAIM':<45} | {'UPDATED'}")
    print("-" * 75)
    for r in rows:
        print(f"{r[0]:<4} | {r[1]:<6.2f} | {r[2]:<5} | {r[3][:43]:<45} | {r[4][:10]}")
    print("=" * 75 + "\n")

def record_contradiction(conn: sqlite3.Connection, claim_id: int, reason: str, penalty: float):
    now = datetime.now().isoformat()
    cursor = conn.cursor()
    cursor.execute("SELECT confidence, contradictions FROM beliefs WHERE id = ?", (claim_id,))
    row = cursor.fetchone()
    if not row:
        print(f"[ERROR] Claim id {claim_id} not found.")
        return

    curr_conf, curr_contr = row
    new_conf = max(0.0, curr_conf - penalty)
    new_contr = curr_contr + 1

    cursor.execute("""
        UPDATE beliefs SET confidence = ?, contradictions = ?, updated_at = ? WHERE id = ?
    """, (new_conf, new_contr, now, claim_id))
    conn.commit()
    print(f"[BELIEF GRAPH] Contradiction logged for ID {claim_id}. Confidence adjusted: {curr_conf:.2f} -> {new_conf:.2f}")

def export_markdown(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("SELECT id, claim, confidence, sources, contradictions FROM beliefs")
    rows = cursor.fetchall()

    md = "# Persistent Evidence & Belief Graph\n\n"
    md += "| ID | Claim | Confidence | Contradictions | Primary Sources |\n"
    md += "|---|---|---|---|---|\n"
    for r in rows:
        md += f"| {r[0]} | {r[1]} | {r[2]:.2f} | {r[4]} | {r[3]} |\n"
    return md

def main():
    parser = argparse.ArgumentParser(description="Hermes Belief & Mission Graph Manager")
    parser.add_argument("--db", type=str, default=str(DEFAULT_DB_PATH), help="Path to SQLite database")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add", help="Add or update a belief")
    add_parser.add_argument("--claim", required=True, type=str, help="Claim statement")
    add_parser.add_argument("--confidence", required=True, type=float, help="Confidence (0.0 - 1.0)")
    add_parser.add_argument("--source", required=True, type=str, help="Source URL or file reference")

    # list
    subparsers.add_parser("list", help="List all beliefs in graph")

    # contradict
    contr_parser = subparsers.add_parser("contradict", help="Log a contradiction against a belief")
    contr_parser.add_argument("--claim-id", required=True, type=int, help="Belief ID")
    contr_parser.add_argument("--reason", required=True, type=str, help="Contradiction reason")
    contr_parser.add_argument("--penalty", type=float, default=0.2, help="Confidence penalty")

    # export
    exp_parser = subparsers.add_parser("export", help="Export graph to markdown")
    exp_parser.add_argument("--output", type=str, default=None, help="Output file path")

    args = parser.parse_args()

    conn = get_connection(pathlib.Path(args.db))

    if args.command == "add":
        add_belief(conn, args.claim, args.confidence, args.source)
    elif args.command == "list":
        list_beliefs(conn)
    elif args.command == "contradict":
        record_contradiction(conn, args.claim_id, args.reason, args.penalty)
    elif args.command == "export":
        md = export_markdown(conn)
        if args.output:
            pathlib.Path(args.output).write_text(md, encoding="utf-8")
            print(f"[BELIEF GRAPH] Exported to {args.output}")
        else:
            print(md)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
