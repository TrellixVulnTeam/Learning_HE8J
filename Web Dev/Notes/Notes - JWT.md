# JWT (Json Web Token)
[Authentication & Refreshing Tokens Implementation - YouTube](https://www.youtube.com/watch?v=xjMP0hspNLE&t=6s)
This is for **authorization** , not **authentication**

Alternative ways include sessions (cookies), but it is vulnerable to CSRF
![[Pasted image 20220601150009.png]]

 It can be easily decoded, but that's not the issue, the server will compare the signature by recreating using the header and payload.
![[Pasted image 20220601150043.png]]   


