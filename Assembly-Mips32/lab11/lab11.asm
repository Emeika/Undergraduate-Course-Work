.data
	prompt:     .asciiz "Enter a string: "    # Prompt message
	count:      .word 0                      # Variable to store the count
	buffer:     .space 256                   # Buffer to store the input string
	newline:    .asciiz "\n"
	str1:       .asciiz "Computer "
	str2:       .asciiz "Science."

.text 
.globl main 
j main

strSplit:
	loop5:
		lb $t1, 0($s4)        # Load a character from the input string
        	beqz $t1, returnSplit # If it's null terminator, exit the loop
        
        	li $v0, 11            # Service number 11 for printing a character
        	move $a0, $t1         # Move the character to $a0 for printing
        	syscall
        
        	addi $s4, $s4, 1      # Increment the input string pointer
        	lb $t1, 0($s4)        # Load the next character from the input string
       	 	beqz $t1, returnSplit # If it's null terminator, exit the loop
        
        	li $v0, 11            # Print the asterisk character
        	li $a0, '*'
        	syscall
        
        	j loop5               
	returnSplit:
	jr $ra

strCat:
	
	loop3:
		lb $t3, 0($s0)   # Load a character from str1
	
		beqz $t3, second    # If it's null terminator, jump to second
		
		addi $s0, $s0, 1   # Increment str1 pointer
		j loop3
	second:
		loop4:
			lb $t4, 0($s1)
		
			beqz $t4, returnCat
			sb $t4, 0($s0)   # Store the character in str1
			addi $s1, $s1, 1   # Increment str2 pointer
			addi $s0, $s0, 1  # Increment str1 pointer
			j loop4
	returnCat:
	sb $zero, 0($s0)         # Add null terminator at the end of str1

	li $v0, 4  #print newline
	la $a0, newline
	syscall 
	
	li $v0, 4
	la $a0, str1  # print string concact
	syscall
	

	jr $ra


strRev:	
	li $v0, 4  #print newline
	la $a0, newline
	syscall 
	
	loop2:
		lb $t2, -1($t0)      # Load current character before the null terminator
   		beqz $t2, return      # Branch to return if null terminator is reached
   		li $v0, 11           # System call to print each character
   		la $a0, ($t2)
   		syscall
    
		addiu $t0, $t0, -1   # Move to previous character
    		j loop2

	return:
	jr $ra

strlen:
	
	li $t1, 0          # Initialize count to 0
	loop:
    		lb $t2, 1($t0)      # Load current character
   		beqz $t2, done      # Branch to done if null terminator is reached
    
    		addiu $t1, $t1, 1   # Increment count
    
    		addiu $t0, $t0, 1   # Move to next character
    		j loop
    
	done:
	jr $ra  
	
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
   	 
   	jal strlen   #function call
   	
   	li $v0, 1
   	move $a0, $t1  #print count
   	syscall
   	
   	jal strRev  # function call to reverse
   	
   	la $s0, str1
   	la $s1, str2
   	
   	jal strCat
   	
   	li $v0, 4  #print newline
	la $a0, newline
	syscall 
   	
   	li $v0, 4
   	la $a0, prompt
   	syscall
   	
    	# Read string 
    	li $v0, 8
    	la $a0, buffer
    	li $a1, 256
   	syscall
    
   	move $s4, $a0  # read the string into $s4
   	
	jal strSplit
	
   	
   	# Exit program
    	li $v0, 10
    	syscall
   	 
    
    
    
    
    
    
    
    
    
    
    
    
