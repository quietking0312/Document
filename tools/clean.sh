#!/bin/bash

set -e

function clean_local_mod() {
	MOD=$1
	git filter-branch -f --prune-empty --index-filter "git rm --ignore-unmatch --cached -rf $MOD" --tag-name-filter cat -- --all
	# gc
	rm -rf .git/refs/original
	git reflog expire --expire=now --all
	git fsck --full --unreachable
	git repack -A -d
	git gc --aggressive --prune=now
	# 提交
	git push --force --all

	git count-objects -v
}

clean_local_mod "a"

echo "clean local ok! remember to new a remote repos to push!!!"
