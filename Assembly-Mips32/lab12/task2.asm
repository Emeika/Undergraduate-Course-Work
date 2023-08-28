.data
	prompt: .asciiz "Enter a string: "
	result: .asciiz "Vowels in string: "
	input: .space 255
	
.text
	li $v0, 4
	la $a0, prompt
	syscall
	
	li $v0, 8
	la $a0, input
	li $a1, 255
	syscall
	
	la $t0, input
	li $t2, 0 # vowel counter
	loop:
		lb	$t1, ($t0)
		beqz	$t1, end # end of string

		beq	$t1, 'a', is_vowel
		beq	$t1, 'e', is_vowel
		beq	$t1, 'i', is_vowel
		beq	$t1, 'o', is_vowel
		beq	$t1, 'u', is_vowel
		
	next_pointer:
		add $t0, $t0, 1 # next pointer
		j loop
		
	is_vowel:
		addi $t2, $t2, 1
		j next_pointer
	
	end:
		li $v0, 4
		la $a0, result
		syscall
		
		li $v0, 1
		la $a0, ($t2)
		syscall