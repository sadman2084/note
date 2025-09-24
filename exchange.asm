.model small
.stack 100h  

.data

a db ?  
b db "first value $"
c db "second value $"


.code
main proc  
    
    mov ax,@data
    mov ds,ax
    
    
    mov ah,1
    int 21h
    mov bl,al
    
    
    mov ah,1
    int 21h
    mov bh,al  
     mov ah,2
            mov dl,0Ah
            int 21h
            
             mov ah,2
            mov dl,0Dh
            int 21h
               
    mov a,bl
    mov bl,bh
    mov bh,a
              
              
     mov ah,9
     lea dx,b
     int 21h
     
       mov ah,2
     mov dl,bl
     int 21h
            
            mov ah,2
            mov dl,0Ah
            int 21h 
            
            mov ah,2
            mov dl,0Dh
            int 21h
     
     mov ah,9
     lea dx,c
     int 21h 
     
     
     mov ah,2
     mov dl,bh
     int 21h
              mov ah,2
            mov dl,0Ah
            int 21h 
            
            mov ah,2
            mov dl,0Dh
            int 21h

mov ah,4ch
int 21h
main endp
end main
            
    
    
    
    