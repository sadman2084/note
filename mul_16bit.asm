.model small
.stack 100h
.code

main proc
    mov ax, 1234h ; first 16-bit number
    mov bx, 0020h ; second 16-bit number
    mul bx
    
  