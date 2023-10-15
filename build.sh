cp -r predist dist
cp -r src/ dist/boot/python/axelnt/

genisoimage --eltorito-boot -o axelnt.iso dist

rm -rf dist/
