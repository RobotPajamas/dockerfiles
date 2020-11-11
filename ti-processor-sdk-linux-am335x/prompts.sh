#!/usr/bin/expect
 
set timeout 1
spawn ./setup.sh
expect "Verify and enter your Linux username below" { send "root\n" }
expect "Do you have administrator privilieges" { send "y\n" }
interact
