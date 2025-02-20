#!/bin/bash

echo "Hello World"


# for loop example
for n in a b c;
do 
    echo $n
done

for n in a, b, c;
do 
    echo $n
done

#  range based loop
# in a range based loop we declare the start, stop and  incrementing value. By default it's one 
for n in {1..5};
do
    echo $n
done

# to add a specific incrementaor
for n in {1..10..2};
do
    echo "Value : $n"
done

# working with variables
name="Techie world"
echo $name

# concatenation
foo="Hello"
greet="$foo wolrd"
echo $greet

# foo="Hello"
# foo="${foo} World"
# echo "${foo}"
# > Hello World