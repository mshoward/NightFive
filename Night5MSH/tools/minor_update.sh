#!/bin/sh
echo `cat VERSION` && echo " --> " && echo `semver -i minor \`cat VERSION\``
semver -i minor `cat VERSION` > VERSION


