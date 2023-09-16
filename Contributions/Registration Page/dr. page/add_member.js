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

// for upload image
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

// for upload signature
const image_input1 = document.querySelector("#image_input1")
var uploaded_image = "";

image_input1.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector("#display_image1").style.backgroundImage = `url(${uploaded_image})`
    })
    reader.readAsDataURL(this.files[0]);
})

