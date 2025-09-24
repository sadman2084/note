  mov ax, 16h 
    mov cx, 0h 
    mov bx, 1h 

next_guess:
    mov dx, 0h
    mov ax, 16h
    div bx      

    add ax, bx   
    shr ax, 1   
    cmp ax, cx   
    je done      
    mov cx, ax   
    inc bx       
    jmp next_guess
done:
    mov ax, cx  
             
    add ax,30h
    
    mov ah,2
    mov dx,ax
    int 21h
    