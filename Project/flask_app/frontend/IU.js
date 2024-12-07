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
        foodPic1.src = uploaded[0];
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
        foodPic2.src = uploaded[1];
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
        foodPic3.src = uploaded[2];
        foodPic3.style.visibility = 'visible';
        foodPic2.style.visibility = 'hidden';
        foodPic1.style.visibility = 'hidden';
    }
}





// form.addEventListener("submit", function(e) {
//     e.preventDefault();
//     if (uploaded.length == 3) {
//         console.log(...form)
//         const formdata = new FormData();
//         for (let i = 0; i < 3; i++) {
//             formdata.append("picture" + i + 1, uploaded[i]);
//         }
//         fetch("http://127.0.0.1:5000/image_upload", {
//             method: "POST",
//             body: formdata,
//         })
        
        

//     }
    
    
// })

