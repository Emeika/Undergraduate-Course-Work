# Write a MIPS assembly program that takes an input from the user character by character of a 
# string until enter is pressed. Count the number of capital characters and store them in a 
# variable named count. (No need of display

.data
prompt:     .asciiz "Enter a string: "    # Prompt message
count:      .word 0                      # Variable to store the count
buffer:     .space 256                   # Buffer to store the input string

    .text
    .globl main

main:
    # Print prompt
    li $v0, 4
    la $a0, prompt
    syscall
    
    # Read string
    li $v0, 8
    la $a0, buffer
    li $a1, 256
    syscall
    
    # Process string
    move $t0, $a0       # Move string address to $t0
    li $t1, 0           # Initialize count to zero
    
loop:
    lb $t2, 0($t0)      # Load current character
    beqz $t2, done      # Branch to done if null terminator is reached
    
    # Check if the character is a capital letter (ASCII range: 65-90)
    blt $t2, 65, next   # Skip if character is less than 'A'
    bgt $t2, 90, next   # Skip if character is greater than 'Z'
    addiu $t1, $t1, 1   # Increment count
    
next:
    addiu $t0, $t0, 1   # Move to next character
    j loop
    
done:
    # Store count in memory
    sw $t1, count
    
    # Exit program
    li $v0, 10
    syscall
