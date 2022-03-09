#!/usr/bin/env bash

git config --global user.name "kgregory413"
git config --global user.email "kgregory413@gmail.com"

git checkout master

git pull

getQuarter(){
    year=$(date +%Y)
    case $(date +%m) in
    01|02|03) qtr="Q1" ;;
    04|05|06) qtr="Q2" ;;
    07|08|09) qtr="Q3" ;;
    10|11|12) qtr="Q4" ;;
    esac
}

getPreviousQuarter(){
    year=$(date +%Y)
    case $(date +%m) in
    01|02|03) let year=year-1; qtr="Q4" ;;
    04|05|06) qtr="Q1" ;;
    07|08|09) qtr="Q2" ;;
    10|11|12) qtr="Q3" ;;
    esac
}

getQuarter

branch_name=alpha-$year-$qtr

git branch $branch_name
git push
git checkout $branch_name

echo Creating Sentinel File IAMALPHA !
touch IAMALPHA
git add IAMALPHA
git commit -m "Sentinel File Added"
git push

getPreviousQuarter
previous_branch=alpha-$year-$qtr

echo Comparing old branch $previous_branch to the new branch $branch_name !
git diff $previous_branch $branch_name
