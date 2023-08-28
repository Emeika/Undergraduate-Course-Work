.text
	li $t0, 1
loop1:	beq $t0, 10, endloop
	move $a0, $t0
	li $v0, 1
	syscall
	addi $t0, $t0, 1
	j loop1
	
endloop:
	li $v0, 10
	syscall
