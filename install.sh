#!/bin/bash

PATH_CONFIG="/automate"
PATH_SCRIPT="./script/"
PATH_INSTALL="/usr/local/bin"
PATH_LOCAL_DIR="."

function Create_Directory_automate(){
	if [[ ! -e $PATH_CONFIG ]];
	then
		mkdir $PATH_CONFIG
	fi
}

function Create_Directory_app(){
	local path_config_app="$PATH_CONFIG/$1"
	echo "$path_config_app"
	if [[ -e  $path_config_app ]];
	then
		rm -rf $path_config_app
	fi

	mkdir $path_config_app
}

function Install_script (){
	cp "$PATH_SCRIPT/$1.py" "$PATH_INSTALL/$1"
	chmod a+x "$PATH_INSTALL/$1"
}

#comprobamos parametros recibidos
if [[ -z $1  ]];
then
	echo "no name app to install recieved."
	exit
fi


Create_Directory_automate
Create_Directory_app "$1"
Install_script "$1"
