.model small
.stack 100h
.code
main proc
    mov al,25h      
    mov bl,12h     
    
    sub al,bl       
    add al,30h     
    
    mov ah,2
    mov dl,al
    int 21h         
    
    mov ah,4ch
    int 21h
main endp
end main
