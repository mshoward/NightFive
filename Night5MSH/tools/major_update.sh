#!/bin/sh
echo `cat VERSION` && echo " --> " && echo `semver -i major \`cat VERSION\``
semver -i major `cat VERSION` > VERSION


