// proper SERVIR site variables

// let html ='<iframe class="strong-shadow" width="710" height="380" src="https://datastudio.google.com/embed/reporting/1d3dd761-2f92-4d2c-b01e-e0e13d3b1201/page/67PxC" frameborder="0" style="border:0" allowfullscreen></iframe>';
// let html2 = '<iframe class="strong-shadow" width="710" height="380" src="https://datastudio.google.com/embed/reporting/0b331800-a601-4e52-b16f-a9db08f49801/page/67PxC" frameborder="0" style="border:0" allowfullscreen></iframe>';

// variables for site at korarsenault repo

let html ='<iframe class="strong-shadow" width="710" height="380" src="https://datastudio.google.com/embed/reporting/bb70e8fa-9b56-4b2d-8377-40e57ab1d703/page/67PxC" frameborder="0" style="border:0" allowfullscreen></iframe>';
let html2 = '<iframe class="strong-shadow" width="710" height="380" src="https://datastudio.google.com/embed/reporting/d4abae97-5b45-4148-b754-e8eab14ce437/page/67PxC" frameborder="0" style="border:0" allowfullscreen></iframe>';

let x = document.querySelector("#lightFrame")

bgColor = window.getComputedStyle(document.body, null).getPropertyValue('background-color');

if (bgColor == 'rgb(255, 255, 255)'){
    x.innerHTML=html
}
else if (bgColor == 'rgb(33, 33, 33)'){
    x.innerHTML=html2
}
else {
    x.innerHTML='<p>null</p>'
}
