#!/bin/sh
echo `cat VERSION` && echo " --> " && echo `semver -i patch \`cat VERSION\``
semver -i patch `cat VERSION` > VERSION


