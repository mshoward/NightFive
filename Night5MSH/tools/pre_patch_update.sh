#!/bin/sh
echo `cat VERSION` && echo " --> " && echo `semver -i prepatch --preid alpha \`cat VERSION\``
semver -i prepatch --preid alpha `cat VERSION` > VERSION


