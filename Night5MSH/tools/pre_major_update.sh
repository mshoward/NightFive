#!/bin/sh
echo `cat VERSION` && echo " --> " && echo `semver -i premajor --preid alpha \`cat VERSION\``
semver -i premajor --preid alpha `cat VERSION` > VERSION


