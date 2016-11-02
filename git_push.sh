#!/bin/bash

echo "This script push changes to github"
git add .
echo "add all files changed"
git commit -m "$1"
echo "commit changes"
git push
echo "push to github"
