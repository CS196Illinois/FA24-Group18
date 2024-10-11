let foodPic1 = document.getElementById("foodPic1");
let foodPic2 = document.getElementById("foodPic2");
let foodPic3 = document.getElementById("foodPic3");

let uploaded = [];

let inputP = document.getElementById("connectIU");
let inputPc = document.getElementById("takeP");
let Pic1 = document.getElementById("Pic1");
let Pic2 = document.getElementById("Pic2");
let Pic3 = document.getElementById("Pic3");
let count = 0;


inputP.onchange = function(){
    switch(count) {
        case 0:
            foodPic1.style.visibility = 'visible';
            foodPic1.src = URL.createObjectURL(inputP.files[0]);
            uploaded[0] = URL.createObjectURL(inputP.files[0]);
            Pic2.style.backgroundColor = "#778271";
            Pic3.style.backgroundColor = "#778271";
            Pic1.style.backgroundColor = "#F5F5F5";
            count++;
            break;
        case 1:
            foodPic1.style.visibility = 'hidden';
            foodPic2.style.visibility = 'visible';
            foodPic2.src = URL.createObjectURL(inputP.files[0]);
            uploaded[1] = URL.createObjectURL(inputP.files[0]);
            Pic1.style.backgroundColor = "#778271";
            Pic3.style.backgroundColor = "#778271";
            Pic2.style.backgroundColor = "#F5F5F5";
            count++;
            break;
        case 2:
            foodPic2.style.visibility = 'hidden';
            foodPic3.style.visibility = 'visible';
            foodPic3.src = URL.createObjectURL(inputP.files[0]);
            uploaded[2] = URL.createObjectURL(inputP.files[0]);
            Pic1.style.backgroundColor = "#778271";
            Pic2.style.backgroundColor = "#778271";
            Pic3.style.backgroundColor = "#F5F5F5";
            count++;
            break;
        case 3:
            return;
        

    }
    
}




inputPc.onchange = function(){
    switch(count) {
        case 0:
            foodPic1.style.visibility = 'visible';
            foodPic1.src = URL.createObjectURL(inputPc.files[0]);
            uploaded[0] = URL.createObjectURL(inputPc.files[0]);
            Pic2.style.backgroundColor = "#778271";
            Pic3.style.backgroundColor = "#778271";
            Pic1.style.backgroundColor = "#F5F5F5";
            count++;
            break;
        case 1:
            foodPic1.style.visibility = 'hidden';
            foodPic2.style.visibility = 'visible';
            foodPic2.src = URL.createObjectURL(inputPc.files[0]);
            uploaded[1] = URL.createObjectURL(inputPc.files[0]);
            Pic1.style.backgroundColor = "#778271";
            Pic3.style.backgroundColor = "#778271";
            Pic2.style.backgroundColor = "#F5F5F5";
            count++;
            break;
        case 2:
            foodPic2.style.visibility = 'hidden';
            foodPic3.style.visibility = 'visible';
            foodPic3.src = URL.createObjectURL(inputPc.files[0]);
            uploaded[2] = URL.createObjectURL(inputPc.files[0]);
            Pic1.style.backgroundColor = "#778271";
            Pic2.style.backgroundColor = "#778271";
            Pic3.style.backgroundColor = "#F5F5F5";
            count++;
            break;
        case 3:
            return;

    }
}

Pic1.onclick = function(){
    if (uploaded[0]) {
        Pic2.style.backgroundColor = "#778271";
        Pic3.style.backgroundColor = "#778271";
        Pic1.style.backgroundColor = "#F5F5F5";
        foodPic1.src = URL.createObjectURL(uploaded[0]);
        foodPic1.style.visibility = 'visible';
        foodPic2.style.visibility = 'hidden';
        foodPic3.style.visibility = 'hidden';

    } 
}

Pic2.onclick = function(){
    if (uploaded[1]) {
        Pic1.style.backgroundColor = "#778271";
        Pic3.style.backgroundColor = "#778271";
        Pic2.style.backgroundColor = "#F5F5F5";
        foodPic2.src = URL.createObjectURL(uploaded[1]);
        foodPic2.style.visibility = 'visible';
        foodPic1.style.visibility = 'hidden';
        foodPic3.style.visibility = 'hidden';
    }
    

}
Pic3.onclick = function(){
    if (uploaded[2]) {
        Pic1.style.backgroundColor = "#778271";
        Pic2.style.backgroundColor = "#778271";
        Pic3.style.backgroundColor = "#F5F5F5";
        foodPic3.src = URL.createObjectURL(uploaded[2]);
        foodPic3.style.visibility = 'visible';
        foodPic2.style.visibility = 'hidden';
        foodPic1.style.visibility = 'hidden';
    }
}

