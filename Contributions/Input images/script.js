const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn");
        allInput = form.querySelectorAll(".first input");

nextBtn.addEventListener("click", ()=> {
    allInput.forEach(input => {
        if(input.value != ""){
            form.classList.add('secActive');
        }else{
            form.classList.remove('secActive');
        
        }
    })
})

const image_input = document.querySelector("#image_input")
var uploaded_image = "";

image_input.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector("#display_image").style.backgroundImage = `url(${uploaded_image})`
    })
    reader.readAsDataURL(this.files[0]);
})