console.log('I am connected!!')
let email;
var emailfield=document.querySelector('#email');
// console.log(emailfield);
document.querySelector('#email').addEventListener("change", getValue);
const getValue=(e)=>{
    console.log(e.target.value);
}