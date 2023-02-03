#! /bin/bash

#directory verification
directory=$(pwd)


if which qrcode >/dev/null; then
sleep 1
echo ""
echo -e "$blue(qrcode)$nc ................................................... Instalado [$green✓$nc]"
else
sleep 1
echo -e "$red(qrcode)$nc No instalado [$red✗$nc]"
sleep 1
echo -e "\e[1;32mInstalando qrcode ...\e[0m"
sleep 3
pip install qrcode
fi
