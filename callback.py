# This script updates commit author details

def rewrite_commit(commit):
    # Add both team members
    commit.author_name = b'laviza & jiya'
    commit.author_email = b'laviza8548.beaift24@gmail.com'

    commit.committer_name = b'laviza & jiya'
    commit.committer_email = b'jiya8541.beaift24@gmail.com'

    return commit