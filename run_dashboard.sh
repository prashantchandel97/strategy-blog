#!/bin/bash
cd "$(dirname "$0")"
streamlit run dashboard.py --server.port 8502 --server.headless false
