cp -r predist dist
cp -r src/ dist/boot/python/axelnt/

sudo apt install syslinux-utils -y

xorriso \
  -outdev ./axelnt.iso -blank as_needed \
  -joliet on \
  -map dist / \
  -volid "AXELNT"
sudo isohybrid ./axelnt.iso
rm -rf dist/
