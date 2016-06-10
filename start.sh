#!/bin/bash
tmux kill-session -t rrrbot
tmux new-session -d -s rrrbot python rrrbot.py
