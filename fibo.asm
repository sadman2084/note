.model small
.stack 100h

.data
    first db 0
    second db 1
    fibo db ?
    n db ?             

.code
main proc
    mov ax, @data
    mov ds, ax

     
    
    mov ah, 1
    int 21h
    sub al, 30h       
    mov n, al

   
    mov dl, '0'
    mov ah, 2
    int 21h
    mov dl, ' '
    int 21h

   
    mov dl, '1'
    mov ah, 2
    int 21h
    mov dl, ' '
    int 21h

    
    mov cl, 2          

FIB_LOOP:
    cmp cl, n
    jge END_PROGRAM   

    
    mov al, first
    add al, second
    mov fibo, al

   
    mov al, second
    mov first, al

    mov al, fibo
    mov second, al

   
    mov dl, fibo
    add dl, 30h       
    mov ah, 2
    int 21h

  
    mov dl, ' '
    mov ah, 2
    int 21h

    inc cl
    jmp FIB_LOOP

END_PROGRAM:
    mov ah, 4Ch
    int 21h
main endp
end main
