.data
arrl: .word 1, 2, 3, 4, 5
arr2: .word 6, 7, 8, 9, 0
sum: .word 0, 0, 0, 0, 0

.text
    la $s0, arrl      
    la $s1, arr2      
    la $s3, sum  
    
    lw $t0 ,0($s0)
    lw $t1 ,0($s1)
    add $t2 ,$s0 ,$s1
    sw $t2 ,0($s3)
    
    
    lw $t0 ,4($s0)
    lw $t1 ,4($s1)
    add $t2 ,$s0 ,$s1
    sw $t2 ,4($s3)
    
    lw $t0 ,8($s0)
    lw $t1 ,8($s1)
    add $t2 ,$s0 ,$s1
    sw $t2 ,8($s3)
    
    lw $t0 ,12($s0)
    lw $t1 ,12($s1)
    add $t2 ,$s0 ,$s1
    sw $t2 ,12($s3)
    
    lw $t0 ,16($s0)
    lw $t1 ,16($s1)
    add $t2 ,$s0 ,$s1
    sw $t2 ,16($s3)