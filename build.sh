cp -r predist dist
cp -r src/ dist/boot/python/axelnt/

xorriso \
  -outdev ./axelnt.iso -blank as_needed \
  -joliet on \
  -map dist / \
  -volid "AXELNT"

rm -rf dist/
