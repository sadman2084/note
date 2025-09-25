.model small
.stack 100h
.data
    decnum db 0
    binstr db '0000$'   
.code
main proc
    mov ax,@data
    mov ds,ax

  
    mov ah,1
    int 21h
    sub al,30h       
    mov decnum,al

  
    mov cl,4         
    mov si,3        
    mov al,decnum

convert_loop:
    mov ah,0
    mov bl,2
    div bl          
    add ah,30h      
    mov binstr[si],ah
    dec si
    loop convert_loop


    mov ah,9
    lea dx,binstr
    int 21h

    mov ah,4ch
    int 21h
main endp
end main
