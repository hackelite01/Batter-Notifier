clear
echo      
echo -e "                       \e[92m TOOL BY Mayank (HackElite)\e[0m"
echo
echo -e "\e[96m        |-----------------------[V 1]-----------------------|"
echo -e "\e[96m        |-------------------\e[92mSELECT OPTIONS\e[96m--------------------|"
echo -e "\e[96m        |-----------------------------------------------------|"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |                [\e[92m1\e[96m]==> 20%                   |"
echo -e "\e[96m        |                [\e[92m2\e[96m]==> 30%                         |"
echo -e "\e[96m        |                [\e[92m3\e[96m]==> 40%                         |"
echo -e "\e[96m        |                [\e[92m4\e[96m]==> 50%                        |"
echo -e "\e[96m        |                [\e[92m5\e[96m]==> 60%                          |"
echo -e "\e[96m        |                [\e[92m6\e[96m]==> SUBSCRIBE                     |"
echo -e "\e[96m        |                [\e[92m7\e[96m]==> 70%                   |"
echo -e "\e[96m        |                [\e[92m8\e[96m]==> CHAT NOW                      |"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |-----------------------------------------------------|"
echo -e "\e[96m        |---------------------\e[91mHEY HACKER\e[96m----------------------|"
echo -e "\e[96m        |-----------------------------------------------------|"
read -p $'\n\e[1;96m[\e[0m\e[1;92m+\e[0m\e[1;96m] SELECT OPTION: \e[0m' option
if [[ $option == 1 || $option == 01 ]]; then
echo
cd $HOME/Battery-Notifier/core
python 20.py
echo
if [[ $option == 2 || $option == 02 ]]; then
echo
cd $HOME/Battery-Notifier/core
python 30.py
echo
if [[ $option == 3 || $option == 03 ]]; then
echo
cd $HOME/Battery-Notifier/core
python 40.py
echo
if [[ $option == 4 || $option == 04 ]]; then
echo
cd $HOME/Battery-Notifier/core
python 50.py
echo
5if [[ $option == 5 || $option == 05 ]]; then
echo
cd $HOME/Battery-Notifier/core
python 60.py
echo
if [[ $option == 6 || $option == 06 ]]; then
echo
clear
am start -a android.intent.action.VIEW -d https://bit.ly/3z38fRK
echo
if [[ $option == 7 || $option == 07 ]]; then
echo
cd $HOME/Battery-Notifier/core
python 70.py
elif [[ $option == 8 || $option == 08 ]]; then
echo
clear
am start -a android.intent.action.VIEW -d https://t.me/hackelite01
else
printf "                \e[1;92m [!] Invalid option!\e[0m\n"
sleep 1
fi
echo
cd $HOME/Batter-Notifier
