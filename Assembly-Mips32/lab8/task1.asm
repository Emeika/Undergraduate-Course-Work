.data
array1: .word 1, 5, 7, 3, 2, 4, 6, 7, 12, 1
length: .word 10
sum: .word 0

.text
  li $t0, 0
  sw $t0, sum
  
  lw $t1, length
  
  li $t2, 0
  la $t3, array1

loop:

  bge $t2, $t1, res

  lw $t4, ($t3)

  andi $t5, $t4, 1
  beq $t5, $zero, even 

  addi $t2, $t2, 1
  addi $t3, $t3, 4
  j loop

even:
  add $t0, $t0, $t4
  addi $t2, $t2, 1
  addi $t3, $t3, 4
  j loop
res:
  sw $t0, sum
  
  lw $a0, sum
  li $v0, 1
  syscall

  li $v0, 10
  syscall
