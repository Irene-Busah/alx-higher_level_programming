#!/usr/bin/node
// This script prints a message depending on the number of arguments passed
if (process.argv[3]){
    console.log('Arguemnts found');
} else if (process.argv[2]){
    console.log('Argument found');
} else {
    console.log('No argument');
}
