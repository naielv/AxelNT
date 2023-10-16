cp -r src/ dist/AxelNT_2023

sudo apt install syslinux-utils -y

xorriso \
  -outdev ./axelnt.iso -blank as_needed \
  -joliet on \
  -map dist / \
  -volid "AxelNT_23"
sudo isohybrid ./axelnt.iso
rm -rf dist/
