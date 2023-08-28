.data
	space: .asciiz " " 
.text
# Problem 2
	li , $t0, 1
loop2:
	beq $t0, 11, endloop
	mul $s0, $t0, 2
	move $a0, $s0
	li $v0, 1
	syscall
	
	li $v0, 4
	la $a0, space
	syscall
	
	addi $t0, $t0, 1
	j loop2
endloop:
	li $v0, 10
	syscall
