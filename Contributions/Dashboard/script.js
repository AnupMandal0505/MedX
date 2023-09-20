// const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

// allSideMenu.forEach(item=> {
// 	const li = item.parentElement;

// 	item.addEventListener('click', function () {
// 		allSideMenu.forEach(i=> {
// 			i.parentElement.classList.remove('active');
// 		})
// 		li.classList.add('active');
// 	})
// });




// // TOGGLE SIDEBAR
// const menuBar = document.querySelector('#content nav .bx.bx-menu');
// const sidebar = document.getElementById('sidebar');

// menuBar.addEventListener('click', function () {
// 	sidebar.classList.toggle('hide');
// })







// const searchButton = document.querySelector('#content nav form .form-input button');
// const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
// const searchForm = document.querySelector('#content nav form');

// searchButton.addEventListener('click', function (e) {
// 	if(window.innerWidth < 576) {
// 		e.preventDefault();
// 		searchForm.classList.toggle('show');
// 		if(searchForm.classList.contains('show')) {
// 			searchButtonIcon.classList.replace('bx-search', 'bx-x');
// 		} else {
// 			searchButtonIcon.classList.replace('bx-x', 'bx-search');
// 		}
// 	}
// })





// if(window.innerWidth < 768) {
// 	sidebar.classList.add('hide');
// } else if(window.innerWidth > 576) {
// 	searchButtonIcon.classList.replace('bx-x', 'bx-search');
// 	searchForm.classList.remove('show');
// }


// window.addEventListener('resize', function () {
// 	if(this.innerWidth > 576) {
// 		searchButtonIcon.classList.replace('bx-x', 'bx-search');
// 		searchForm.classList.remove('show');
// 	}
// })



// const switchMode = document.getElementById('switch-mode');

// switchMode.addEventListener('change', function () {
// 	if(this.checked) {
// 		document.body.classList.add('dark');
// 	} else {
// 		document.body.classList.remove('dark');
// 	}
// })


// const form = document.querySelector("form"),
//         nextBtn = form.querySelector(".nextBtn");
//         allInput = form.querySelectorAll(".row .input-group");


// nextBtn.addEventListener("click", ()=> {
//     allInput.forEach(input => {
//         if(input.value != ""){
//             form.classList.add('secActive');
//         }else{
//             form.classList.remove('secActive');
//         }
//     })
// })


// const image_input1 = document.querySelector("#image_input1")
// var uploaded_image = "";

// image_input1.addEventListener("change", function(){
//     const reader = new FileReader();
//     reader.addEventListener("load", () => {
//         uploaded_image = reader.result;
//         document.querySelector("#display_image1").style.backgroundImage = `url(${uploaded_image})`
//     })
//     reader.readAsDataURL(this.files[0]);
// })



// const image_input2 = document.querySelector("#image_input2")
// var uploaded_image = "";

// image_input2.addEventListener("change", function(){
//     const reader = new FileReader();
//     reader.addEventListener("load", () => {
//         uploaded_image = reader.result;
//         document.querySelector("#display_image2").style.backgroundImage = `url(${uploaded_image})`
//     })
//     reader.readAsDataURL(this.files[0]);
// })

// const image_input3 = document.querySelector("#image_input3")
// var uploaded_image = "";

// image_input3.addEventListener("change", function(){
//     const reader = new FileReader();
//     reader.addEventListener("load", () => {
//         uploaded_image = reader.result;
//         document.querySelector("#display_image3").style.backgroundImage = `url(${uploaded_image})`
//     })
//     reader.readAsDataURL(this.files[0]);
// })



// const image_input4 = document.querySelector("#image_input4")
// var uploaded_image = "";

// image_input4.addEventListener("change", function(){
//     const reader = new FileReader();
//     reader.addEventListener("load", () => {
//         uploaded_image = reader.result;
//         document.querySelector("#display_image4").style.backgroundImage = `url(${uploaded_image})`
//     })
//     reader.readAsDataURL(this.files[0]);
// })



// const image_input5 = document.querySelector("#image_input5")
// var uploaded_image = "";

// image_input5.addEventListener("change", function(){
//     const reader = new FileReader();
//     reader.addEventListener("load", () => {
//         uploaded_image = reader.result;
//         document.querySelector("#display_image5").style.backgroundImage = `url(${uploaded_image})`
//     })
//     reader.readAsDataURL(this.files[0]);
// })