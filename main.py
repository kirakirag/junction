#!/usr/bin/env python3
"""Small CLI that exposes the DB helpers from `db.py`.

Commands:
- load: ensure the database `uber_hackathon_db` exists and load the Excel file from ./data
- run-query: run an example SQL query and print the result
"""
from __future__ import annotations

import argparse
import logging
from typing import Optional

from db import start_db, load_uber_data, example_query


logger = logging.getLogger("junction.main")


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="CLI for DB helpers")
	sub = parser.add_subparsers(dest="cmd", required=True)

	p_load = sub.add_parser("load", help="Ensure DB and load Uber Excel from ./data")
	p_load.add_argument("--host", default="localhost")
	p_load.add_argument("--port", default=5432, type=int)
	p_load.add_argument("--user", default="postgres")
	p_load.add_argument("--password", help="Postgres password (will prompt if omitted)")
	p_load.add_argument("--table", default="uber_hackathon_data")

	p_q = sub.add_parser("run-query", help="Run an example SQL query against the DB")
	p_q.add_argument("sql", help="SQL to execute")
	p_q.add_argument("--host", default="localhost")
	p_q.add_argument("--port", default=5432, type=int)
	p_q.add_argument("--user", default="postgres")
	p_q.add_argument("--password", help="Postgres password (will prompt if omitted)")

	parser.add_argument("--debug", action="store_true")
	return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
	args = parse_args(argv)
	logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO, format="%(levelname)s: %(message)s")

	if args.cmd == "load":
		engine = start_db(host=args.host, port=args.port, user=args.user, password=args.password, dbname="uber_hackathon_db")
		load_uber_data(engine, data_folder="data", filename="uber_hackathon_v2_mock_data.xlsx", table_name=args.table)
		logger.info("Load complete")

	elif args.cmd == "run-query":
		engine = start_db(host=args.host, port=args.port, user=args.user, password=args.password, dbname="uber_hackathon_db")
		df = example_query(engine, args.sql)
		print(df)

	else:
		logger.error("Unknown command: %s", args.cmd)
		return 2

	return 0


if __name__ == "__main__":
	raise SystemExit(main())

