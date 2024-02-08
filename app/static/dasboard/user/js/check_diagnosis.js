
    const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn");
        allInput = form.querySelectorAll(".row .input-group");



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



const image_input2 = document.querySelector("#image_input2")
var uploaded_image = "";

image_input2.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector("#display_image2").style.backgroundImage = `url(${uploaded_image})`
    })
    reader.readAsDataURL(this.files[0]);
})

const image_input3 = document.querySelector("#image_input3")
var uploaded_image = "";

image_input3.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector("#display_image3").style.backgroundImage = `url(${uploaded_image})`
    })
    reader.readAsDataURL(this.files[0]);
})



const image_input4 = document.querySelector("#image_input4")
var uploaded_image = "";

image_input4.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector("#display_image4").style.backgroundImage = `url(${uploaded_image})`
    })
    reader.readAsDataURL(this.files[0]);
})



const image_input5 = document.querySelector("#image_input5")
var uploaded_image = "";

image_input5.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector("#display_image5").style.backgroundImage = `url(${uploaded_image})`
    })
    reader.readAsDataURL(this.files[0]);
})
