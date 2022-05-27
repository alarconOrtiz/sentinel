#!/bin/bash
PATH_CONFIG="/automate"
PATH_INSTALL="/usr/local/bin"

function Uninstall_config(){
	local path_config="$PATH_CONFIG/$1"
	if [ -e $path_config  ];
	then 
		rm -rf "$path_config"
	fi
}

function Uninstall_script(){
	local path_script="$PATH_INSTALL/$1"
	if [ -e $path_script ];
	then
		rm -f "$path_script"
	else
		echo "app not currently installed"
		exit
	fi
}

if [[ "$#" -eq "1"  ]];
then
	Uninstall_config "$1"
	Uninstall_script "$1"
	echo "app successfully uninstalled"
else
 	echo "parameters incorrect"
	exit
fi
